from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder
from src.config import EMBEDDING_MODEL

encoder = HuggingFaceEncoder(
    model_name=EMBEDDING_MODEL
)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Tell me the return policy",
        "Return policy for damaged products",
        "Do I get discount with the HDFC credit card?",
        "Discounts available with HDFC card",
        "HDFC card discount details",
        "How can I track my order?",
        "Order tracking steps",
        "Track my order status",
        "What payment methods are accepted?",
        "Accepted payment options",
        "Which payment modes can I use",
        "How long does it take to process a refund?",
        "Refund processing time",
        "When will I get my refund",
        "What is your policy on defective product?",
        "Policy on defective items",
        "Defective product handling",
    ]
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Show nike shoes with 50 percent off",
        "Any nike shoes on half price",
        "Are there any shoes under Rs. 3000?",
        "Shoes below 3000 rupees",
        "Budget shoes under ₹3000",
        "Do you have formal shoes in size 9?",
        "Formal shoes size 9 available",
        "I need size 9 formal shoes",
        "Are there any Puma shoes on sale?",
        "Sale on Puma shoes",
        "Discounted Puma shoes",
        "What is the price of puma running shoes?",
        "Puma running shoes price",
        "Cost of Puma running shoes",
        "Pink Puma shoes in price range 5000 to 1000",
        "Find pink Puma shoes between ₹1000 and ₹5000",
    ]
)

smalltalk = Route(
    name='smalltalk',
    utterances=[
        "How are you?",
        "Hope you're doing well",
        "Are you doing okay",
        "What is your name?",
        "Tell me your name",
        "Who are you",
        "Are you a robot?",
        "Are you human or bot",
        "You're a robot right",
        "What are you?",
        "Tell me what you are",
        "Explain yourself",
        "What do you do?",
        "What's your job",
        "Your role",
    ]
)

router = SemanticRouter(
    routes=[faq, sql, smalltalk],
    encoder=encoder,
    auto_sync="local"
)

if __name__ == "__main__":
    print(router("What is the return policy of the products?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
    print(router("How are you?").name)
