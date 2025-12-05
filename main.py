import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db

def load_data():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM benhnhan")

    rows = cursor.fetchall()
    for r in rows:
        tree.insert("", tk.END, values=r)

    conn.close()

def add_patient():
    ho_ten = entry_name.get()
    gioi_tinh = gender_var.get()
    ngay_sinh = entry_birth.get()
    dia_chi = entry_address.get()
    ngay_nhap = entry_datein.get()
    chuan_doan = entry_diagnose.get()
    sdt = entry_phone.get()

    conn = connect_db()
    cursor = conn.cursor()
    sql = """
    INSERT INTO benhnhan(ho_ten, gioi_tinh, ngay_sinh,
      dia_chi, ngay_nhap_vien, chuan_doan, sdt)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(sql, (ho_ten, gioi_tinh, ngay_sinh,
     dia_chi, ngay_nhap, chuan_doan, sdt))
    conn.commit()
    conn.close()

    load_data()
    messagebox.showinfo("Thành công", "Đã thêm bệnh nhân")

def select_item(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if values:
        entry_id.delete(0, tk.END)
        entry_id.insert(0, values[0])  # vẫn lưu mã BN
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])
        gender_var.set(values[2])
        entry_birth.delete(0, tk.END)
        entry_birth.insert(0, values[3])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, values[4])
        entry_datein.delete(0, tk.END)
        entry_datein.insert(0, values[5])
        entry_diagnose.delete(0, tk.END)
        entry_diagnose.insert(0, values[6])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, values[7])

def update_patient():
    ma_bn = entry_id.get()
    ho_ten = entry_name.get()
    gioi_tinh = gender_var.get()
    ngay_sinh = entry_birth.get()
    dia_chi = entry_address.get()
    ngay_nhap = entry_datein.get()
    chuan_doan = entry_diagnose.get()
    sdt = entry_phone.get()

    conn = connect_db()
    cursor = conn.cursor()
    sql = """
    UPDATE benhnhan SET ho_ten=%s, gioi_tinh=%s, ngay_sinh=%s, dia_chi=%s,
    ngay_nhap_vien=%s, chuan_doan=%s, sdt=%s WHERE ma_bn=%s
    """
    cursor.execute(sql, (ho_ten, gioi_tinh, ngay_sinh,
     dia_chi, ngay_nhap, chuan_doan, sdt, ma_bn))
    conn.commit()
    conn.close()

    load_data()
    messagebox.showinfo("Thành công", "Đã cập nhật thông tin bệnh nhân")

def delete_patient():
    ma_bn = entry_id.get()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM benhnhan WHERE ma_bn=%s", (ma_bn,))
    conn.commit()
    conn.close()

    load_data()
    messagebox.showinfo("Thành công", "Đã xóa bệnh nhân")

def search_patient():
    name_keyword = entry_search.get().strip()
    gender_keyword = gender_search_var.get()

    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()
    cursor = conn.cursor()

    # Truy vấn linh hoạt
    query = "SELECT * FROM benhnhan WHERE 1=1"
    params = []

    if name_keyword != "":
        query += " AND ho_ten LIKE %s"
        params.append("%" + name_keyword + "%")

    if gender_keyword != "Tất cả":
        query += " AND gioi_tinh=%s"
        params.append(gender_keyword)

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()

    for r in rows:
        tree.insert("", tk.END, values=r)

    conn.close()

root = tk.Tk()
root.title("Quản lý bệnh nhân")
root.geometry("1100x600")

form = tk.Frame(root)
form.pack(side=tk.TOP, fill=tk.X)

labels = ["Họ tên:", "Giới tính:", "Ngày sinh:", "Địa chỉ:",
 "Ngày nhập viện:", "Chuẩn đoán:", "SĐT:"]

for i, text in enumerate(labels):
    tk.Label(form, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="w")

# Entry Mã BN tàng hình
entry_id = tk.Entry(form)
# Không grid => tàng hình

entry_name = tk.Entry(form); entry_name.grid(row=0, column=1)

# Combobox giới tính
gender_var = tk.StringVar()
entry_gender = ttk.Combobox(form, textvariable=gender_var, values=["Nam", "Nữ"], state="readonly")
entry_gender.grid(row=1, column=1)

entry_birth = tk.Entry(form); entry_birth.grid(row=2, column=1)
entry_address = tk.Entry(form); entry_address.grid(row=3, column=1)
entry_datein = tk.Entry(form); entry_datein.grid(row=4, column=1)
entry_diagnose = tk.Entry(form); entry_diagnose.grid(row=5, column=1)
entry_phone = tk.Entry(form); entry_phone.grid(row=6, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Thêm", width=12, command=add_patient).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Cập nhật", width=12, command=update_patient).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Xóa", width=12, command=delete_patient).grid(row=0, column=2, padx=5, pady=5)

tk.Label(btn_frame, text="Tìm kiếm tên:").grid(row=1, column=0)
entry_search = tk.Entry(btn_frame); entry_search.grid(row=1, column=1)

tk.Label(btn_frame, text="Giới tính:").grid(row=1, column=3)
gender_search_var = tk.StringVar(value="Tất cả")
gender_search = ttk.Combobox(btn_frame, textvariable=gender_search_var,
                             values=["Tất cả", "Nam", "Nữ"], state="readonly")
gender_search.grid(row=1, column=4)

tk.Button(btn_frame, text="Tìm", width=12, command=search_patient).grid(row=1, column=2)

tree = ttk.Treeview(root, columns=("id", "name", "gender", "birth",
 "address", "datein", "diagnose", "phone"), show="headings", height=10)
tree.pack(fill=tk.BOTH, expand=True)

col_names = ["Mã BN", "Họ tên", "Giới tính", "Ngày sinh",
 "Địa chỉ", "Ngày nhập viện", "Chuẩn đoán", "SĐT"]
for i, col in enumerate(col_names):
    tree.heading(i, text=col)

tree.bind("<ButtonRelease-1>", select_item)

load_data()
root.mainloop()
