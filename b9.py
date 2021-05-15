a = [[]] * 3
a[1].append(1)
print(a)
# Kết quả của bài sẽ trả về [[1], [1], [1]] 
# Vì khi a = [[]] * 3 sẽ có kết quả là [[], [], []]
# Khi ta gián phần tử thứ a[1] thì nó sẽ đề cập đến danh sách lớn bên ngoài chứa 3 danh sách con thì nó sẽ gán 3 danh sách con bằng 1