'''Product IDs and quality status: 
products = [ 
    (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
• Display failed product IDs.  
• Count passed and failed products.  
• Calculate pass percentage.  
• Stop checking if 3 failures are found.'''
# Product IDs and quality status
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0
failed_ids = []

# Check products
for product_id, status in products:
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
        failed_ids.append(product_id)

    # Stop checking if 3 failures are found
    if fail_count == 3:
        print("3 failures found. Stopping inspection.")
        break

# Calculate pass percentage
total_checked = pass_count + fail_count
pass_percentage = (pass_count / total_checked) * 100

# Display results
print("Failed Product IDs:", failed_ids)
print("Passed Products:", pass_count)
print("Failed Products:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")