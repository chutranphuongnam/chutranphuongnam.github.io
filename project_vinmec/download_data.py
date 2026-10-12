#!/usr/bin/env python3
"""
Tải bộ dữ liệu Diabetes 130-US hospitals (UCI id=296) về data/diabetic_data.csv
Thử lần lượt 3 cách; dừng ở cách đầu tiên thành công.
Chạy: python download_data.py
"""
import os, sys, subprocess
from pathlib import Path

OUT = Path("data"); OUT.mkdir(exist_ok=True)
TARGET = OUT / "diabetic_data.csv"

def pip(pkg):
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", pkg], check=True)

def via_ucimlrepo():
    # Bản ĐẦY ĐỦ (101766 x ~50 cột, giữ nguyên các cột thuốc) — ưu tiên
    pip("ucimlrepo")
    from ucimlrepo import fetch_ucirepo
    ds = fetch_ucirepo(id=296)
    df = ds.data.features.copy()
    df["readmitted"] = ds.data.targets
    df.to_csv(TARGET, index=False)
    return df.shape

def via_openml():
    # Fallback qua OpenML (sklearn)
    pip("scikit-learn")
    from sklearn.datasets import fetch_openml
    ds = fetch_openml(data_id=43874, as_frame=True)   # Diabetes 130 US
    ds.frame.to_csv(TARGET, index=False)
    return ds.frame.shape

def via_kaggle():
    # Cần sẵn kaggle.json (~/.kaggle/). Xác nhận slug trước khi dùng.
    pip("kaggle")
    slug = os.environ.get("KAGGLE_SLUG", "brandao/diabetes")
    subprocess.run(["kaggle", "datasets", "download", "-d", slug,
                    "-p", str(OUT), "--unzip"], check=True)
    import pandas as pd
    csv = next(OUT.glob("*.csv"))
    if csv != TARGET: csv.rename(TARGET)
    return pd.read_csv(TARGET).shape

def via_uci_direct():
    # Tải trực tiếp từ UCI Archive (đầy đủ 101766 dòng x 50 cột, không cần pip package)
    import urllib.request, pandas as pd
    url = "https://archive.ics.uci.edu/static/public/296/data.csv"
    urllib.request.urlretrieve(url, TARGET)
    df = pd.read_csv(TARGET)
    return df.shape

for name, fn in [("uci_direct", via_uci_direct),
                 ("ucimlrepo", via_ucimlrepo),
                 ("openml", via_openml),
                 ("kaggle", via_kaggle)]:
    try:
        shape = fn()
        print(f"[OK] Tải qua {name}: {shape} -> {TARGET}")
        sys.exit(0)
    except Exception as e:
        print(f"[FAIL] {name}: {e}")

print("\n[!] Cả 3 cách thất bại (thường do agent bị chặn mạng).")
print("    Tải thủ công 1 lần tại UCI (id 296) hoặc Kaggle, giải nén,")
print("    rồi đặt file vào: data/diabetic_data.csv")
sys.exit(1)
