# cosmic-backend-app
Simple backend application using FastAPI, Python and MongoDB.

**Data Modelling**:

* cosmiccloud [**database consists of following collections**]
  * product_catalogue_category
    - consists of category of items - Fridge/TV,etc. which we sell
  * product_catalogue_items
    - 
  * product_inventory
    - every product in catalogue can be present in multiple warehouses
    - 

**product_catalogue collection**:
```json
  {
    "_id": {
      "$oid": "65b62ffa8eb4a5e09d2f094a"
    },
    "name": "samsung-tv",
    "primary_uom": "Piece",
    "price_without_gst_on_base_uom": 26000,
    "gst_percentage": {
      "cgst": 9.00,
      "sgst": 9.00,
      "igst": 18.00
    },
    "available_quantity_in_inventory": 100,
		"secondary_uom_conversion": [
      {
        "uom": "Box",
        "conversion_factor": 10.0,
        "discounts": [
          
        ]
      }
    ],
    "is_active": true,
    "created_by": 1,
    "created_at_ts": "2024-01-15T10:30:00Z",
    "modified_by": 1,
    "modified_at_ts": "2024-01-15T12:30:00Z",
    "audit_data": [
      {
        "audit_type": "update",
        "entity_key": "price_without_gst_on_base_uom",
        "new_price": 26000,
        "old_price": 25000,
        "modified_by": 1,
        "modified_at_ts": "2024-01-15T12:30:00Z"
      },
      {
        "audit_type": "insert",
        "entity_key": "secondary_uom_conversion",
        "modified_by": 1,
        "modified_at_ts": "2024-01-15T12:45:00Z"
      }
    ]
  }
```
