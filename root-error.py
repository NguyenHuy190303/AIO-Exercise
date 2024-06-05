def md_nre_single_sample(y, y_hat, n, p):
    """Tính MD_nRE cho một cặp giá trị y và y_hat.

    Args:
        y: Giá trị thực tế.
        y_hat: Giá trị dự đoán.
        n: Căn bậc n để áp dụng.
        p: Bậc của hàm loss.

    Returns:
        Giá trị MD_nRE.
    """
    if y < 0 or y_hat < 0:
        raise ValueError("Cả y và y_hat phải là các giá trị không âm.")

    root_diff = abs(y**(1/n) - y_hat**(1/n))
    return root_diff**p