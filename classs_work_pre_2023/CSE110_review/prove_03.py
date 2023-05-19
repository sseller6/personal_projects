#Use int(), float(), or str() for this assignment.
child_price = float(input('What\'s the price of a child\'s meal? '))
adult_price = float(input('What\'s the price of a adult\'s meal? '))
child_amount = int(input('How many children are there? '))
adult_amount = int(input('How many adults are there? '))
sales_tax_rate = int(input('What is the sales tax rate? '))

subtotal = (child_price * child_amount) + (adult_price * adult_amount)
sales_tax = (sales_tax_rate/100) * subtotal
total = (subtotal + sales_tax)
print(f'''
Subtotal: ${subtotal:.2f} 
Sales Tax: ${sales_tax:.2f}
Total: ${total:.2f} 
''')
payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print(f'Change: ${change:.2f}')