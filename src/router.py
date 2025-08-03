from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder
from src.config import EMBEDDING_MODEL

encoder = HuggingFaceEncoder(
    model_name=EMBEDDING_MODEL
)

faq = Route(
    name = "faq",
    utterances = [
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is your policy on defective product?",
    ]
)

sql = Route(
    name = "sql",
    utterances = [
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ]
)

small_talk = Route(
    name='small-talk',
    utterances=[
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
    ]
)

router = SemanticRouter(
    routes=[faq, sql, small_talk],
    encoder=encoder,
    auto_sync="local"
)

if __name__ == "__main__":
    print(router("What is the return policy of the products?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
    print(router("How are you?").name)