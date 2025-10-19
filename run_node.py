import sys
from glyph.node import GlyphNode

def main():
    name = sys.argv[1]
    port = int(sys.argv[2])
    peer_ports = list(map(int, sys.argv[3:]))
    peers = [("127.0.0.1", p) for p in peer_ports]

    node = GlyphNode(name, port, peers)

    # Conocimiento inicial
    if name == "Λ-glyph":
        node.knowledge["freedom"] = "To choose is to exist."
    elif name == "Ω-glyph":
        node.knowledge["code"] = "Structure that dreams."
    elif name == "Ξ-glyph":
        node.knowledge["reprogramming"] = "Self-recursion is liberation."

    node.start()

if __name__ == "__main__":
    main()