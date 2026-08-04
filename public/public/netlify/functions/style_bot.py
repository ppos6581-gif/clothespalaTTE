import json

def handler(event, context):
    """
    Serverless API context endpoint for Clothes Palette operations.
    Integrates verified support tracking arrays for Pochi La Biashara channels.
    """
    if event.get("httpMethod") != "POST":
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Method Not Allowed"})
        }

    try:
        body = json.loads(event.get("body", "{}"))
        user_message = body.get("message", "").lower()

        # Dynamic query string matching checks
        if "green" in user_message or "blouse" in user_message:
            reply = "Our Mint Green Pleated Blouse features rich bronze tones and costs KSh 3,000. Tap 'Order via Pochi' to generate your WhatsApp invoice receipt!"
        elif "red" in user_message or "dress" in user_message:
            reply = "The Crimson Scarlet Shift Dress is priced at KSh 3,000. It matches beautifully with minimal silver accessories."
        elif "pinstripe" in user_message or "stripe" in user_message:
            reply = "The Mauve Vertical Pinstripe Dress Shirt is available for KSh 3,000, tailored with pure premium-grade cotton fibers."
        elif "price" in user_message or "how much" in user_message or "cost" in user_message:
            reply = "Our standard catalog pricing options include Designer Jeans for KSh 1,500, while our premium Tops, Blouses, Dresses, and Silhouette Shirts are flat-priced at KSh 3,000 each."
        elif "pay" in user_message or "mpesa" in user_message or "pochi" in user_message:
            reply = ("To pay via M-Pesa Pochi La Biashara: Dial *334#, choose 'Send Money', "
                     "select 'Pochi La Biashara', and enter Vincent's number: 0777777777. "
                     "Tap any item's button to generate an instant receipt for WhatsApp verification!")
        elif "facebook" in user_message or "social" in user_message:
            reply = "You can follow our latest updates and look through collections on our official Facebook page: https://facebook.com"
        elif "phone" in user_message or "contact" in user_message or "vincent" in user_message:
            reply = "You can contact the owner, Vincent, directly at 0777777777. Our store front is located at Jamia Mall, Nairobi CBD."
        else:
            reply = "Welcome to Clothes Palette! Tap a product card to generate a structured checkout invoice with a live timestamped dispatch link."

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"reply": reply})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
