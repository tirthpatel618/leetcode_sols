# Example Coupon
#
# Exactly one of percent_discount and amount_discount will be non-null (error if not).
# The two 'minimum_...' values can each be null or non-null.
coupon = { 'category': 'fruit',
  'percent_discount': 15,
  'amount_discount': None,
  'minimum_num_items_required': 2,
  'minimum_amount_required': 10.00
}

coupon1 = {
    'category': 'fruit',
  'percent_discount': None,
  'amount_discount': 12,
  'minimum_num_items_required': 2,
  'minimum_amount_required': 10.00
}

coupon2 = {
    'category': 'fruit',
  'percent_discount': None,
  'amount_discount': None,
  'minimum_num_items_required': 2,
  'minimum_amount_required': 10.00
}

coupon3 = {
    'category': 'fruit',
  'percent_discount': 15,
  'amount_discount': None,
  'minimum_num_items_required': 3,
  'minimum_amount_required': 10.00
}

# Example Cart
cart = [ {'price': 2.00, 'category': 'fruit'},
  {'price': 20.00, 'category': 'toy'},
  {'price': 5.00, 'category': 'clothing'},
  {'price': 8.00, 'category': 'fruit'}
]

def price_paid(coupon, cart):
    #throw an error if both the discounts are populated, or if neither fo them are
    if (coupon['percent_discount'] == None and coupon['amount_discount'] == None) or (coupon['percent_discount'] != None and coupon['amount_discount'] != None):
        raise Exception("Error in discounts")
    
    category_items = 0
    # num items required 
    if coupon['minimum_num_items_required'] != None:
        
        for item in cart:
            if item["category"] == coupon["category"]:
                category_items += 1
    category_spend = 0
    #minimum spend
    if coupon['minimum_amount_required'] != None:
        for item in cart:
            if item["category"] == coupon["category"]:
                category_spend += item["price"]
    
    items_required = True if coupon['minimum_num_items_required'] == None or category_items >= coupon['minimum_num_items_required'] else False
    spend_required = True if coupon['minimum_amount_required'] == None or category_spend >= coupon['minimum_amount_required'] else False

    cart_total_w_category = 0
    cart_total = 0
    for item in cart:
        if item["category"] != coupon["category"]:
            cart_total += item["price"]
        cart_total_w_category += item["price"]
      
    if items_required and spend_required:
        if coupon['percent_discount'] != None:
            category_total = category_spend * ((1 - (coupon['percent_discount']  / 100)))
        else:
            category_total = category_spend - coupon["amount_discount"]
            if category_total < 0:
                category_total = 0
    else:
        return cart_total_w_category
    
    cart_total += category_total
     
    return cart_total 

    
    
print(price_paid(coupon3, cart))


[
  {'price': 2.00, 'category': 'fruit'},
  {'price': 20.00, 'category': 'toy'},
  {'price': 5.00, 'category': 'clothing'},
  {'price': 8.00, 'category': 'fruit'}
]

[
  { 'categories': ['clothing', 'toy'],
    'percent_discount': None,
    'amount_discount': 6,
    'minimum_num_items_required': None,
    'minimum_amount_required': None
  },
  { 'categories': ['fruit'],
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
   }
]


# if theres a coupon that has multiple categories, you want to give the max discount
# only one of the discounts can work 
# no coupons can have the same categories

def apply_coupons(coupons, prices):
    for coupon in coupons: 
        if (coupon['percent_discount'] == None and coupon['amount_discount'] == None) or (coupon['percent_discount'] != None and coupon['amount_discount'] != None):
            raise Exception("Error in discounts")
    
    category_list = []
    for coupon in coupons:
        for category in coupon["categories"]:
            if category in category_list:
                raise Exception("Error in coupon categories")
            category_list.append(category)
    
    for coupon in coupons:
        #min items
        differences = []
        for category in coupon["categories"]:
            category_items = 0
            # num items required 
            if coupon['minimum_num_items_required'] != None:
                for item in cart:
                    if item["category"] == category:
                        category_items += 1
            
            category_spend = 0
            if coupon['minimum_amount_required'] != None:
                for item in cart:
                    if item["category"] == category:
                        category_spend += item["price"]

            items_required = True if coupon['minimum_num_items_required'] == None or category_items >= coupon['minimum_num_items_required'] else False
            spend_required = True if coupon['minimum_amount_required'] == None or category_spend >= coupon['minimum_amount_required'] else False
            if not (items_required or spend_required):
                difference = 0
                differences.append(difference)
                continue
                
            category_spend = 0
            for item in cart:
                if item["category"] == category:
                    category_spend += item["price"]

            if coupon['percent_discount'] != None:
                discount_total = category_spend * ((1 - (coupon['percent_discount']  / 100)))
                difference = category_spend - discount_total
            else:
                discount_total = category_spend - coupon["amount_discount"]
                if category_total < 0:
                    category_total = 0
                difference = category_spend - discount_total
            differences.append(difference)
        
            #difference = original_category_price - discounted_category_price
        



        




    
    

        
    