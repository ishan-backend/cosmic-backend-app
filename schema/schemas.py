def product_catalogue_entity_serializer(ProductCatalogue) -> dict:
    return {
        "id": str[ProductCatalogue["_id"]],
        "product_name": str[ProductCatalogue["name"]]
    }


def product_catalogue_list_serializer(ProductCatalogueEntities) -> list:
    return [product_catalogue_entity_serializer(pc) for pc in ProductCatalogueEntities]


def purchase_order_entity_serializer(PurchaseOrder) -> dict:
    return {
        "id": str[PurchaseOrder["_id"]],
        "created_by_name": str[PurchaseOrder["created_by_name"]]
    }


def po_list_serializer(PurchaseOrderEntities) -> list:
    return [purchase_order_entity_serializer(po) for po in PurchaseOrderEntities]
