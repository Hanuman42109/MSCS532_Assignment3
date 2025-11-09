import random

# ---------------------------
# Hash Table with Chaining
# ---------------------------
class HashTable:
    def __init__(self, capacity=8):
        """
        Initialize the hash table.
        :param capacity: initial number of buckets (slots)
        """
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0  # number of elements

    def _hash(self, key):
        """
        Simple universal hash function for integers and strings.
        """
        if isinstance(key, int):
            return key % self.capacity
        elif isinstance(key, str):
            # Polynomial rolling hash for strings
            p = 31
            hash_value = 0
            for char in key:
                hash_value = (hash_value * p + ord(char)) % self.capacity
            return hash_value
        else:
            raise TypeError("Unsupported key type")

    def _load_factor(self):
        """Compute load factor (α = n / m)."""
        return self.size / self.capacity

    def _resize(self):
        """Double the table size and rehash all existing keys."""
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    # ---------------------------
    # Core Operations
    # ---------------------------
    def insert(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        bucket.append((key, value))
        self.size += 1

        # Resize if load factor > 0.75
        if self._load_factor() > 0.75:
            self._resize()

    def search(self, key):
        """Search for a key and return its value (or None if not found)."""
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def display(self):
        """Print hash table structure (for debugging/demo)."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# ---------------------------
# Demo / Test
# ---------------------------
if __name__ == "__main__":
    print("=== Hash Table with Chaining Demo ===\n")

    ht = HashTable()

    # Insert random key-value pairs
    for i in range(10):
        key = f"key{i}"
        value = random.randint(1, 100)
        ht.insert(key, value)

    ht.display()
    print("\nSize:", ht.size)
    print("Load factor:", round(ht._load_factor(), 2))

    # Search test
    test_key = "key5"
    print(f"\nSearching for '{test_key}':", ht.search(test_key))

    # Delete test
    print(f"Deleting '{test_key}' ->", ht.delete(test_key))
    print(f"Searching '{test_key}' after deletion ->", ht.search(test_key))

    # Resize demonstration
    print("\nInserting additional elements to trigger resizing...")
    for i in range(20, 35):
        ht.insert(f"item{i}", random.randint(1, 100))
    print("New capacity after resizing:", ht.capacity)

    print("\n✅ Hash Table operations completed successfully.")