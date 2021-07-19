import json
class DataManager:

    def __init__(self, product_dict):
        self.product_dict = product_dict

    def check_if_item_in_data_file(self):
        product_list = []
        target_name_index = []
        try:
            with open('data/product.json', mode='r') as products:
                try:
                    product_list = json.load(products)

                except json.decoder.JSONDecodeError:
                    pass

        except FileNotFoundError:
            with open('data/product.json', mode='w', encoding='utf-8') as f:
                json.dump([], f)

        finally:
            in_list = False
            for i in product_list:
                product_entry = i
                if self.product_dict['Product Name'] == product_entry['Product Name']:
                    target_name_index = product_list.index(i)
                    if product_entry['Target Price'] != self.product_dict['Target Price']:
                        print("Need to update the price")
                        self.upsert_price(self.product_dict, target_name_index)
                    in_list = True
                    break  # <---- should break and stop reading at the first van richten

            if in_list == False:
                with open('data/product.json', mode='w', encoding='utf-8') as products:
                    product_list.append(self.product_dict)
                    json.dump(product_list, products, indent=2)

    def upsert_price(self, product_dict, index_of_entry_to_update):
        # 1. Bring json file into buffer.
        with open('data/product.json', mode='r', encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)

        # 2. Edit the data while it is in the buffer, don't try to write it directly to the file.
        data[index_of_entry_to_update]['Target Price'] = product_dict['Target Price']

        # 3. Write the amended file to the buffer.
        # This seems really inefficient. Think of new way to do this.
        with open('data/product.json', mode='w', encoding='utf-8') as jsonFile:
            json.dump(data, jsonFile, indent=2)

    def check_if_price_below_target(self):

        products_to_buy = []

        with open('data/product.json', mode='r', encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)

        for i in data:
            if i['Price'] < i['Target Price']:
                products_to_buy.append(i)

        return products_to_buy
