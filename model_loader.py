from models import customer, menu_item, order, order_detail, review, payment, promotion, resource
from dependencies.database import engine

def index():
    customer.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
    order.Base.metadata.create_all(engine)
    order_detail.Base.metadata.create_all(engine)
    review.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    resource.Base.metadata.create_all(engine)

if __name__ == "__main__":
    index()
