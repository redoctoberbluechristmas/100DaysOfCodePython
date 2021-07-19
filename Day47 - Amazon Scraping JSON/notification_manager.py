import smtplib


class NotificationManager:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_email_password = sender_password

    def send_email(self, products_to_buy, target_email):

        for i in products_to_buy:
            target_index = products_to_buy.index(i)
            product_name = products_to_buy[target_index]['Product Name']
            target_price = products_to_buy[target_index]['Target Price']
            product_price = products_to_buy[target_index]['Price']
            product_url = products_to_buy[target_index]['URL']
            savings = product_price - target_price

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.sender_email, password=self.sender_email_password)
                connection.sendmail(
                    from_addr=self.sender_email,
                    to_addrs=target_email,
                    msg=f"Subject:{product_name} on sale.\n\n{product_name} is now on sale for ${savings} below your "
                        f"target price of {target_price}. It can be found here: {product_url}. "
                )