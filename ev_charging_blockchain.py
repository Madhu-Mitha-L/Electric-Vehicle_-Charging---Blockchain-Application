import hashlib
import time
import json
import uuid

# ------------------ Blockchain Core ------------------
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, {"Genesis Block": "EV Charging System"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def display_chain(self):
        print("\n🔗 Blockchain Ledger:")
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash[:20]}...")
            print(f"Previous Hash: {block.previous_hash[:20]}...\n")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True


# ------------------ User & Station ------------------
class User:
    def __init__(self, user_id, balance=1000):
        self.user_id = user_id
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return f"User(ID={self.user_id}, Balance={self.balance})"


class Station:
    def __init__(self, station_id, owner, rate=10, balance=0):
        self.station_id = station_id
        self.owner = owner
        self.rate = rate
        self.balance = balance

    def __str__(self):
        return f"Station(ID={self.station_id}, Owner={self.owner}, Rate={self.rate}, Balance={self.balance})"


# ------------------ EV Charging System ------------------
class EVChargingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.users = {}
        self.stations = {}
        self.completed_sessions = set()

    # ---------------- User Management ----------------
    def register_user(self, user_id, balance=1000):
        if user_id in self.users:
            print(f"❌ User ID {user_id} already exists.")
            return
        self.users[user_id] = User(user_id, balance)
        print(f"✅ User '{user_id}' registered with balance {balance}")

    # ---------------- Station Management ----------------
    def register_station(self, station_id, owner, rate=10):
        if station_id in self.stations:
            print(f"❌ Station ID {station_id} already exists.")
            return
        self.stations[station_id] = Station(station_id, owner, rate)
        print(f"✅ Station '{station_id}' registered with owner '{owner}' at rate {rate}")

    # ---------------- Recharge Wallet ----------------
    def recharge_wallet(self, user_id, amount):
        if user_id not in self.users:
            print(f"❌ Invalid User ID '{user_id}'. Please register first.")
            return
        if amount <= 0:
            print("❌ Recharge amount must be positive.")
            return
        self.users[user_id].balance += amount
        print(f"💰 Wallet recharged: User {user_id} new balance = {self.users[user_id].balance}")

    # ---------------- Start Charging ----------------
    def start_charging(self, user_id, station_id, units):
        # Strict validation
        if user_id not in self.users:
            print(f"❌ Invalid User ID '{user_id}'.")
            return
        if station_id not in self.stations:
            print(f"❌ Invalid Station ID '{station_id}'. Please register the station first.")
            return
        if units <= 0:
            print("❌ Units must be positive.")
            return
        if units > 50:
            print("❌ Maximum 50 units allowed per session.")
            return

        user = self.users[user_id]
        station = self.stations[station_id]
        cost = units * station.rate

        if user.balance < cost:
            print(f"❌ Insufficient balance! Needed {cost}, Available {user.balance}")
            return

        # Unique session ID
        session_id = str(uuid.uuid4())[:8]
        while session_id in self.completed_sessions:
            session_id = str(uuid.uuid4())[:8]
        self.completed_sessions.add(session_id)

        # Process transaction
        user.balance -= cost
        station.balance += cost

        # Low balance warning
        if user.balance < 100:
            print(f"⚠️ Warning: User {user_id} balance is low ({user.balance} Rupees)")

        transaction = {
            "session_id": session_id,
            "user_id": user_id,
            "station_id": station_id,
            "units": units,
            "rate": station.rate,
            "cost": cost,
            "timestamp": time.ctime()
        }

        # Record in user's transaction history
        user.transactions.append(transaction)

        # Add block to blockchain
        new_block = Block(len(self.blockchain.chain), transaction, self.blockchain.get_latest_block().hash)
        self.blockchain.add_block(new_block)

        print(f"⚡ Charging Complete! Session ID: {session_id}")
        print(f"User {user_id} charged {units} units at Station {station_id} (Cost={cost})")

    # ---------------- Show Wallet Balances & Transactions ----------------
    def show_balances(self):
        print("\n👤 Users:")
        for user in self.users.values():
            print(user)
            for tx in user.transactions:
                print(f"   ↪ Session {tx['session_id']} | {tx['units']} units at {tx['station_id']} | Cost={tx['cost']} | {tx['timestamp']}")
        print("\n🏭 Stations:")
        for station in self.stations.values():
            print(station)


# ------------------ Interactive CLI ------------------
if __name__ == "__main__":
    system = EVChargingSystem()
    exit_symbol = "."

    # ---------------- Register Initial Users ----------------
    system.register_user("Sharon", 500)
    system.register_user("Deeraj", 800)
    system.register_user("Preetha", 300)
    system.register_user("Nithin", 1000)
    system.register_user("Arun", 700)
    system.register_user("Arul", 600)

    # ---------------- Register Initial Stations ----------------
    system.register_station("StationA", "OwnerA", rate=10)
    system.register_station("StationB", "OwnerB", rate=12)
    system.register_station("StationC", "OwnerC", rate=8)
    system.register_station("StationD", "OwnerD", rate=11)

    print("\n🛡️ Welcome to Secure Blockchain EV Charging System")
    print(f"Type '{exit_symbol}' anytime to exit.\n")

    while True:
        print("\nOptions:")
        print("1. Start Charging")
        print("2. Recharge Wallet")
        print("3. Show Wallet & Transaction History")
        print(f"Type '{exit_symbol}' to Exit\n")

        choice = input("Enter option number: ").strip()
        if choice == exit_symbol:
            print("👋 Exiting system.")
            break

        if choice == "1":
            user_id = input("Enter your User ID: ").strip()
            if user_id == exit_symbol:
                continue
            station_id = input("Enter Station ID: ").strip()
            if station_id == exit_symbol:
                continue
            units_input = input("Enter units to charge: ").strip()
            if units_input == exit_symbol:
                continue
            if not units_input.isdigit():
                print("❌ Units must be a positive number.\n")
                continue
            units = int(units_input)
            system.start_charging(user_id, station_id, units)

        elif choice == "2":
            user_id = input("Enter your User ID to recharge: ").strip()
            if user_id == exit_symbol:
                continue
            amount_input = input("Enter amount to recharge: ").strip()
            if amount_input == exit_symbol:
                continue
            if not amount_input.isdigit():
                print("❌ Amount must be a positive number.\n")
                continue
            amount = int(amount_input)
            system.recharge_wallet(user_id, amount)

        elif choice == "3":
            system.show_balances()

        else:
            print("❌ Invalid option. Try again.")

    # Display final blockchain ledger and validity
    system.blockchain.display_chain()
    print(f"\n✅ Blockchain valid? {system.blockchain.is_chain_valid()}")
