import pandas as pd

# Đọc file CSV
url = "https://drive.google.com/uc?export=download&id=10Is5JOIQw6TdX1w3o79L9nBhyfn_xM09"
df = pd.read_csv(url)

# In ra số hàng và cột của dữ liệu
print("Số hàng và cột của dữ liệu ban đầu:")
print(df.shape)

# Thêm dữ liệu mới
new_data = {
    "case_id": [7000005],
    "province": ["Seoul"],
    "city": ["Gurogu"],
    "group": [False],
    "infection_case": ["Itaewon Clubs"],
    "confirmed": [46],
    "latitude": [37.508163],
    "longitude": [127.044374],
}

new_row = pd.DataFrame(new_data)

# Thêm dòng mới vào DataFrame
df = pd.concat([df, new_row], ignore_index=True)

# In ra số hàng và cột của dữ liệu sau khi thêm
print("\nSố hàng và cột của dữ liệu sau khi thêm:")
print(df.shape)

# In ra DataFrame sau khi thêm
print("\nDữ liệu sau khi thêm:")
print(df)
