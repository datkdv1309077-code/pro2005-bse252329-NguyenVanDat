class Nguoi:
    def __init__(self, ten, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không hợp lệ!")
        self._ten = ten
        self._tuoi = tuoi
    def get_ten(self):
        return self._ten
    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi phải >= 0")
        self._tuoi = tuoi
    def __str__(self):
        return f"Tên: {self._ten}, Tuổi: {self._tuoi}"
    def xin_chao(self):
        return f"Xin chào, tôi là {self._ten}"
    @classmethod
    def thong_tin_loai(cls):
        return "Đây là lớp Nguoi"
    @staticmethod
    def kiem_tra_tuoi(tuoi):
        return tuoi >= 0
    def __eq__(self, other):
        return self._ten == other._ten and self._tuoi == other._tuoi
class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        self._mssv = mssv
    def __str__(self):
        return f"{super().__str__()}, MSSV: {self._mssv}"
def bai9():
    sv1 = SinhVien("An", 20, "SV01")
    sv2 = SinhVien("An", 20, "SV01")
    print(sv1)
    print(sv1.xin_chao())
    print(Nguoi.thong_tin_loai())
    print(Nguoi.kiem_tra_tuoi(10))
    print("So sánh == :", sv1 == sv2)
    sv1.set_tuoi(25)
    print("Sau khi sửa:", sv1)