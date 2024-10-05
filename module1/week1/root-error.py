def md_nre_single_sample(y, y_hat, n, p):
    """
    Tính toán Mean Difference of nth Root Error cho một cặp giá trị y và y_hat (không dùng numpy).

    Args:
        y: Giá trị thực tế.
        y_hat: Giá trị dự đoán.
        n: Căn bậc n để áp dụng cho cả y và y_hat.
        p: Bậc của hàm loss (thường là 1 hoặc 2).

    Returns:
        Giá trị MD_nRE cho cặp y và y_hat.
    """
    # Kiểm tra điều kiện đầu vào (đơn giản hóa như yêu cầu)
    assert y >= 0 and y_hat >= 0, "Cả y và y_hat phải không âm."
    assert n > 0, "Căn bậc n phải dương."
    assert p > 0, "Bậc của hàm loss phải dương."

    # Tính toán MD_nRE (sử dụng hàm lũy thừa và giá trị tuyệt đối có sẵn)
    return abs(y**(1/n) - y_hat**(1/n))**p
