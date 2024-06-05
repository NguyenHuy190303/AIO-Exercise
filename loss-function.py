import random
import math

def exercise3():
    """
    Hàm tính toán và in ra các giá trị mất mát (loss) cho các mẫu dự đoán.
    """

    while True:
        num_samples_str = input("Nhập số lượng mẫu (số nguyên) được tạo ra: ")
        if num_samples_str.isnumeric():
            num_samples = int(num_samples_str)
            break
        else:
            print("Số lượng mẫu phải là một số nguyên.")

    loss_name = input("Nhập tên hàm mất mát (MAE, MSE, RMSE): ").upper()  # Chuyển thành chữ hoa để dễ so sánh

    total_loss = 0  # Biến lưu tổng loss để tính RMSE cuối cùng
    
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == "MAE":
            loss = abs(target - predict)
        elif loss_name == "MSE":
            loss = (target - predict) ** 2
        elif loss_name == "RMSE":
            loss = math.sqrt((target - predict) ** 2)
        else:
            print("Tên hàm mất mát không hợp lệ.")
            return  # Thoát khỏi hàm nếu tên không hợp lệ

        total_loss += loss  # Cộng dồn loss cho RMSE

        print(f"Tên hàm mất mát: {loss_name}, Mẫu: {i}, Dự đoán: {predict:.2f}, Giá trị thực: {target:.2f}, Mất mát: {loss:.2f}")

    if loss_name == "RMSE":
        final_rmse = math.sqrt(total_loss / num_samples)
        print(f"RMSE cuối cùng: {final_rmse:.2f}")

# Gọi hàm để bắt đầu chương trình
exercise3()
