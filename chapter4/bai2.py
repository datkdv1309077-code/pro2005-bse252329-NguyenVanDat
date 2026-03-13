def tinh_diem_trung_binh(ds):
    tong = sum(ds.values())
    so_sv = len(ds)

    return tong / so_sv

sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

tb = tinh_diem_trung_binh(sinh_vien)

print("Điểm trung bình:", tb)