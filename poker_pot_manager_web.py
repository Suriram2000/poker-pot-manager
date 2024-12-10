import streamlit as st

# Poker Pot Manager
class PokerPotManager:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if name in self.players:
            st.warning(f"Player '{name}' already exists!")
        else:
            self.players[name] = 0
            st.success(f"Player '{name}' added!")

    def edit_pot(self, name, amount):
        if name not in self.players:
            st.error(f"Player '{name}' does not exist!")
        else:
            self.players[name] += amount

    def remove_player(self, name):
        if name in self.players:
            del self.players[name]
            st.success(f"Player '{name}' removed!")
        else:
            st.error(f"Player '{name}' does not exist!")

    def reset_pots(self):
        for player in self.players:
            self.players[player] = 0
        st.success("All pots reset to 0!")

    def get_total_pot(self):
        return sum(self.players.values())

# Streamlit UI
def main():
    st.title("Poker Pot Manager")
    manager = PokerPotManager()

    with st.sidebar:
        st.header("Add Player")
        name = st.text_input("Player Name", key="player_name")
        if st.button("Add Player", key="add_player_button"):
            manager.add_player(name)

    # Display each player in separate boxes
    if manager.players:
        st.subheader("Current Players")
        for player, pot in manager.players.items():
            with st.container():
                st.write(f"**{player}**")
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.write(f"Pot: ${pot}")
                with col2:
                    if st.button(f"+1 ({player})", key=f"add_{player}"):
                        manager.edit_pot(player, 1)
                with col3:
                    if st.button(f"-1 ({player})", key=f"sub_{player}"):
                        manager.edit_pot(player, -1)

        # Reset and Remove All Players
        st.subheader("Actions")
        if st.button("Reset All Pots", key="reset_button"):
            manager.reset_pots()

        if st.button("Remove All Players", key="remove_all_button"):
            manager.players = {}
            st.success("All players removed!")

        # Display Total Pot
        st.subheader("Total Pot")
        st.write(f"Total Pot: ${manager.get_total_pot()}")

if __name__ == "__main__":
    main()
