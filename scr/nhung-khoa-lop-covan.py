import pandas as pd
import json
import numpy as np
import random

ho_vn = ["Nguyễn", "Trần", "Lê", "Phạm", "Huỳnh", "Hoàng", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
lot_nam = ["Văn", "Hữu", "Đức", "Minh", "Quốc", "Thành", "Công", "Đình", "Mạnh", "Quang", ]
ten_nam = ["Hùng", "Cường", "Tuấn", "Dũng", "Sơn", "Hải", "Long", "Vinh", "Phúc", "Thịnh", "Khánh"]
lot_nu = ["Thị", "Thu", "Ngọc", "Thanh", "Mỹ", "Kim", "Hồng", "Diệu", "Phương", "Bích"]
ten_nu = ["Lan", "Huệ", "Mai", "Hoa", "Hương", "Hằng", "Thảo", "Dung", "Tuyết", "Oanh", "Vân", "Trinh"]
dau_so = ["090", "091", "098", "097", "038", "088", "070", "093"]

def rand_phone():
    """Tạo số điện thoại ngẫu nhiên"""
    return random.choice(dau_so) + "".join([str(random.randint(0, 9)) for _ in range(7)])

def rand_father(full_name_sv):
    """Tạo tên Cha dựa theo Họ của Sinh viên"""
    if pd.isna(full_name_sv) or str(full_name_sv).strip() == "":
        ho_sv = random.choice(ho_vn)
    else:
        ho_sv = str(full_name_sv).strip().split()[0] 
    return f"{ho_sv} {random.choice(lot_nam)} {random.choice(ten_nam)}"

def rand_mother():
    """Tạo tên Mẹ ngẫu nhiên"""
    return f"{random.choice(ho_vn)} {random.choice(lot_nu)} {random.choice(ten_nu)}"

THONG_TIN_LOP = {
  "_id": {
    "$oid": "69415880e8b05fa2caba0366"
  },
  "ma_lop": "DA23DT",
  "hoc_ky": "2025-2026",
  "nam_nhap_hoc": 2023,
  "so_luong_sinh_vien": 17,
  
  
  "co_van_hoc_tap": {
  "_id": {
    "$oid": "693ff8f124f61dc097af28d7"
  },
  "ma_gv": "01",
  "ten_gv": "Cao Phương Thảo",
  "sdt": "0766719277",
  "email": "cpthao@tvu.edu.vn"

}}

THONG_TIN_KHOA = {
  "_id": {
    "$oid": "694158e1e8b05fa2caba0370"
  },
  "ma_khoa": "DT",
  "ten_khoa": "Điện-điện tử",
  "dia_chi": "C5"
}


try:
    # Đọc file Excel
    df = pd.read_excel('DA23DT.xlsx', engine='openpyxl')
    
    # Làm sạch tên cột
    df.columns = df.columns.str.strip()
    
    # Xử lý MSSV và Ngày sinh
    df['MSSV'] = df['MSSV'].astype(str).str.strip().replace('nan', '0')
    df['Ngày sinh'] = pd.to_datetime(df['Ngày sinh'], format='%d/%m/%Y', errors='coerce')
    
    def safe_to_iso(dt):
        return dt.isoformat() if pd.notna(dt) else None
    df['Ngày sinh'] = df['Ngày sinh'].apply(safe_to_iso)

    mongodb_docs = []

    # Vòng lặp xử lý từng sinh viên
    for index, row in df.iterrows():
        
        # --- XỬ LÝ SỐ ĐIỆN THOẠI SINH VIÊN ---
        raw_sdt = row.get('SĐT')
        sdt_final = str(raw_sdt) if pd.notna(raw_sdt) else ""
        if sdt_final.endswith('.0'): sdt_final = sdt_final[:-2]
        if sdt_final.isdigit() and len(sdt_final) == 9: sdt_final = '0' + sdt_final

        # --- XỬ LÝ ID & ĐỊA CHỈ ---
        ma_sv_str = row['MSSV']
        ma_sv_int = int(ma_sv_str) if ma_sv_str.isdigit() and ma_sv_str != '0' else None 

        raw_dia_chi = row.get('HỘ KHẨU THƯỜNG TRÚ')
        dia_chi_final = "0" if pd.isna(raw_dia_chi) or str(raw_dia_chi).strip() == "" else str(raw_dia_chi).strip()
        
        # --- 🔥 TẠO DỮ LIỆU GIA ĐÌNH (RANDOM) TẠI ĐÂY 🔥 ---
        ten_cha_fake = rand_father(row.get('HỌ TÊN'))
        sdt_cha_fake = rand_phone()
        ten_me_fake = rand_mother()
        sdt_me_fake = rand_phone()
        
        raw_email = row.get('Email')
        # Kiểm tra nếu email trong excel bị trống (NaN) thì tự tạo, ngược lại thì dùng giá trị trong excel
        if pd.isna(raw_email) or str(raw_email).strip() == "":
            email_final = f"{ma_sv_int}@st.tvu.edu.vn"
        else:
            email_final = str(raw_email).strip()

        # Tạo document sinh viên
        student_doc = {
            "ma_sinh_vien": ma_sv_int,
            "ten_sinh_vien": row.get('HỌ TÊN'),
            "gioi_tinh": row.get('GT'),
            "ngay_sinh": row['Ngày sinh'],
            "dan_toc": row.get('Dân tộc'),
            "ton_giao": row.get('Tôn giáo'),
            "sdt": sdt_final,
            "email": email_final, # Đã sửa lỗi cộng chuỗi int
            "chuyen_nganh": row.get('Chuyên ngành'),
            "bac_dao_tao": row.get('Bậc đào tạo'),
            "he_dao_tao": row.get('Hệ đào tạo'),
            "nien_khoa": row.get('Niên khóa'),
            "trang_thai": row.get('Trạng thái'),

            "thong_tin_lop": THONG_TIN_LOP,
            "thong_tin_khoa": THONG_TIN_KHOA,

            "cmnd_cccd": {
                "ma_so_cccd": str(row.get('SỐ CMT/CCCD', '')).strip(),
                "noi_cap_cccd": "", 
                "ngay_cap": ""
            },
            "dia_chi": {
                "dia_chi_thuong_tru" : dia_chi_final,
                "dia_chi_tam_tru": "",
            },
            
            # --- ĐIỀN DỮ LIỆU GIA ĐÌNH VỪA TẠO ---
            "quan_he_gia_dinh": {
                "ho_ten_cha": ten_cha_fake,
                "sdt_cha": sdt_cha_fake,
                "ho_ten_me": ten_me_fake,
                "sdt_me": sdt_me_fake
            },
        }
        mongodb_docs.append(student_doc)

    # 3. LƯU FILE JSON
    OUTPUT_FILE = 'sinhvien_full.json'
    if mongodb_docs:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(mongodb_docs, f, ensure_ascii=False, indent=4)
        print(f"Đã tạo file JSON (Có Tên/SĐT Cha Mẹ): {OUTPUT_FILE}")
    else:
        print("Không có dữ liệu.")

except Exception as e:

    print(f"Lỗi: {e}")
