# Slice to find beginning items, middle item and ending items

slice_list=["Food","Water","Computer","Game","Meat", "Fan", "Phone"]

# print(slice_list[:3])
# print(slice_list[3:])
start_ = len(slice_list) // 2
end_ = start_+3 
print(slice_list[start_:end_])