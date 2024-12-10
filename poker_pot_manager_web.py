import streamlit as st
import random

# Generate a random color for each player
def get_random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Poker Pot Manager Class
class PokerPotManager:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if name in self.players:
            st.warning(f"Player '{name}' already exists!")
        else:
            self.players[name] = {"pot": 0, "color": get_random_color()}
            st.success(f"Player '{name}' added!")

    def edit_pot(self, name, amount):
        if name not in self.players:
            st.error(f"Player '{name}' does not exist!")
        else:
            self.players[name]["pot"] += amount

    def remove_player(self, name):
        if name in self.players:
            del self.players[name]
            st.success(f"Player '{name}' removed!")
        else:
            st.error(f"Player '{name}' does not exist!")

    def reset_pots(self):
        for player in self.players:
            self.players[player]["pot"] = 0
        st.success("All pots reset to 0!")

    def get_total_pot(self):
        return sum(player["pot"] for player in self.players.values())

# Main App
def main():
    st.title("Poker Pot Manager")
    manager = PokerPotManager()

    # Sidebar for Adding Players
    with st.sidebar:
        st.header("Add Player")
        name = st.text_input("Player Name", key="player_name")
        if st.button("Add Player", key="add_player_button"):
            if name.strip():
                manager.add_player(name.strip())
            else:
                st.warning("Player name cannot be empty!")

    # Display Players and Pots
    if manager.players:
        st.subheader("Current Players")
        for player, details in manager.players.items():
            with st.container():
                color = details["color"]
                pot = details["pot"]

                # Player Box
                st.markdown(
                    f"""
                    <div style="background-color:{color}; padding:10px; border-radius:10px; margin-bottom:10px;">
                        <h3 style="margin:0; color:white;">{player}</h3>
                        <p style="margin:0; color:white;">Pot: ${pot}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Controls for each player
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if st.button(f"+1 ({player})", key=f"add_{player}"):
                        manager.edit_pot(player, 1)
                with col2:
                    if st.button(f"-1 ({player})", key=f"sub_{player}"):
                        manager.edit_pot(player, -1)
                with col3:
                    if st.button(f"Remove ({player})", key=f"remove_{player}"):
                        manager.remove_player(player)

        # Reset and Total Pot Actions
        st.subheader("Actions")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Reset All Pots", key="reset_button"):
                manager.reset_pots()
        with col2:
            if st.button("Remove All Players", key="remove_all_button"):
                manager.players = {}
                st.success("All players removed!")

        # Total Pot
        st.subheader("Total Pot")
        st.write(f"Total Pot: ${manager.get_total_pot()}")

if __name__ == "__main__":
    main()
