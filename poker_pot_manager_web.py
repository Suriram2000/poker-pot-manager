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
        name = st.text_input("Player Name")
        if st.button("Add Player"):
            manager.add_player(name)

    if manager.players:
        st.subheader("Current Pots")
        for player, pot in manager.players.items():
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.write(player)
            with col2:
                st.write(f"${pot}")
            with col3:
                if st.button(f"+1 ({player})", key=f"add_{player}"):
                    manager.edit_pot(player, 1)
            with col4:
                if st.button(f"-1 ({player})", key=f"sub_{player}"):
                    manager.edit_pot(player, -1)

        st.subheader("Actions")
        if st.button("Reset All Pots"):
            manager.reset_pots()

        if st.button("Remove All Players"):
            manager.players = {}
            st.success("All players removed!")

        st.subheader("Total Pot")
        st.write(f"${manager.get_total_pot()}")

if __name__ == "__main__":
    main()
