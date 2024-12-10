import streamlit as st
import random

# Generate a random color for each player
def get_random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Initialize or load the session state for player management
if "players" not in st.session_state:
    st.session_state.players = {}

# Add a new player
def add_player(name):
    if name in st.session_state.players:
        st.warning(f"Player '{name}' already exists!")
    else:
        st.session_state.players[name] = {"pot": 0, "color": get_random_color()}
        st.success(f"Player '{name}' added!")

# Edit the pot value of a player
def edit_pot(name, amount):
    if name in st.session_state.players:
        st.session_state.players[name]["pot"] += amount

# Remove a player
def remove_player(name):
    if name in st.session_state.players:
        del st.session_state.players[name]
        st.success(f"Player '{name}' removed!")

# Reset all pots to 0
def reset_pots():
    for player in st.session_state.players:
        st.session_state.players[player]["pot"] = 0
    st.success("All pots reset to 0!")

# Main application
st.title("Poker Pot Manager")

# Sidebar for adding players
with st.sidebar:
    st.header("Add Player")
    player_name = st.text_input("Player Name")
    if st.button("Add Player"):
        if player_name.strip():
            add_player(player_name.strip())
        else:
            st.warning("Player name cannot be empty!")

# Display players and controls
if st.session_state.players:
    st.subheader("Players")
    for player, data in st.session_state.players.items():
        with st.container():
            # Display player details
            st.markdown(
                f"""
                <div style="background-color:{data['color']}; padding:10px; border-radius:10px; margin-bottom:10px;">
                    <h4 style="margin:0; color:white;">{player}</h4>
                    <p style="margin:0; color:white;">Pot: ${data['pot']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Controls for editing pots and removing players
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"+1 ({player})"):
                    edit_pot(player, 1)
            with col2:
                if st.button(f"-1 ({player})"):
                    edit_pot(player, -1)
            with col3:
                if st.button(f"Remove ({player})"):
                    remove_player(player)

    # Reset and Total Pot
    st.subheader("Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Reset All Pots"):
            reset_pots()
    with col2:
        if st.button("Remove All Players"):
            st.session_state.players = {}
            st.success("All players removed!")

    # Display total pot
    st.subheader("Total Pot")
    total_pot = sum(data["pot"] for data in st.session_state.players.values())
    st.write(f"**Total Pot: ${total_pot}**")

else:
    st.write("No players added yet. Use the sidebar to add players.")
