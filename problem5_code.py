class InventorySystem:
    def __init__(self):
    
        self.inventory = {}
    
    def add_product(self, product_id:str, name:str, quantity:int, price:float):
        if quantity < 0 or price < 0:
            raise Exception("Quantity and price cannot be Negative.")
        
        if product_id in self.inventory:
            self.inventory[product_id]["name"] = name
            self.inventory[product_id]["quantity"] = quantity
            self.inventory[product_id]["price"] = price
        else:
            self.inventory[product_id] = {"name":name, "quantity":quantity, "price":price}
        
    def remove_product(self, product_id:str):
        if product_id in self.inventory:
            del self.inventory[product_id]
            return True
        return False
           
    def get_inventory_value(self):   
       total_value = 0
        
       for product in self.inventory.values():
            total_value += product["quantity"] * product["price"]
       return total_value    
    
    def search_products(self, keyword: str): 
        keyword = keyword.lower()
        results = []
        for pid, product in self.inventory.items():
            if keyword in product["name"].lower():
                results.append({"id": pid, "name":product["name"] , "quantity":product["quantity"] , "price":product["price"]})
            
        return results
        
