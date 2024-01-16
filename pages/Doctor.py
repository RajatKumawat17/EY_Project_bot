import streamlit as st
from streamlit_card import card

def create_horizontal_cards():
    # Define your card content and data
    card_data = [
        {"title": "Arun Kumar", "text": "Cardiologist", "image": "https://s3.envato.com/files/354413107/2072.jpg", "url": ""},
        {"title": "Yash singh", "text": "Gastrologist", "image": "https://img.freepik.com/free-photo/handsome-smiling-medical-professional-examining-with-stethoscope-colored-background_662251-366.jpg?size=626&ext=jpg&ga=GA1.1.1412446893.1704585600&semt=ais", "url": ""},
        {"title": "Anukriti singh", "text": "Gyaenecologist", "image": "https://img.freepik.com/free-photo/attractive-medical-professional-uniform-standing-with-arms-crossed-against-isolated-background_662251-416.jpg?size=626&ext=jpg&ga=GA1.1.1412446893.1704585600&semt=ais", "url": ""},
        # Add more cards as needed
    ]

    # Specify the number of cards to display in each row
    cards_per_row = 3

    # Calculate the number of rows needed
    num_rows = len(card_data) // cards_per_row + (len(card_data) % cards_per_row > 0)

    # Create horizontal scrollable cards
    for row in range(num_rows):
        # Create a row of columns
        cols = st.columns(cards_per_row)

        for col_index, col in enumerate(cols):
            card_index = row * cards_per_row + col_index

            # Check if the card index is within the data range
            if card_index < len(card_data):
                # Create a card in the column using streamlit-card
                with col:
                    has_clicked = card(
                        title=card_data[card_index]["title"],
                        text=card_data[card_index]["text"],
                        image=card_data[card_index]["image"],
                        url=card_data[card_index]["url"]
                    )

def create_horizontal_cards1():
    # Define your card content and data
    card_data = [
        {"title": "Paracetamol", "text": "Medicine", "image": "https://www.onlinechemistuk.net/wp-content/uploads/2019/10/essential-medicines-online-chemist-gorleston-paracetamol-300x206.jpg", "url": ""},
        {"title": "Ibuprofen", "text": "Medicine", "image": "https://www.onlinechemistuk.net/wp-content/uploads/2019/10/essential-medicines-online-chemist-gorleston-ibuprofen-300x253.jpg", "url": ""},
        {"title": "Zantac", "text": "Medicine", "image": "https://www.onlinechemistuk.net/wp-content/uploads/2019/10/essential-medicines-online-chemist-gorleston-loperamide-300x210.jpg", "url": ""},
        # Add more cards as needed
    ]

    # Specify the number of cards to display in each row
    cards_per_row = 3

    # Calculate the number of rows needed
    num_rows = len(card_data) // cards_per_row + (len(card_data) % cards_per_row > 0)

    # Create horizontal scrollable cards
    for row in range(num_rows):
        # Create a row of columns
        cols = st.columns(cards_per_row)

        for col_index, col in enumerate(cols):
            card_index = row * cards_per_row + col_index

            # Check if the card index is within the data range
            if card_index < len(card_data):
                # Create a card in the column using streamlit-card
                with col:
                    has_clicked = card(
                        title=card_data[card_index]["title"],
                        text=card_data[card_index]["text"],
                        image=card_data[card_index]["image"],
                        url=card_data[card_index]["url"]
                    )


# Create a Streamlit app
def main():
    st.title("Patient Dashboard")
    st.subheader("get consultation now :", divider='grey')
    # Call the function to create horizontal scrollable cards
    create_horizontal_cards()

    st.subheader("get medication now :", divider='grey')
    create_horizontal_cards1()

if __name__ == "__main__":
    main()
