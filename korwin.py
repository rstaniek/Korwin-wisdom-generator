import secrets, json, re, getopt, sys

class Korwinator:
    
    def __init__(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.data_size = len(self.data['intro'])
    
    def _element(self, section, look_comma=True):
        element = str(self.data[section][secrets.randbits(6) % self.data_size])
        if not element.startswith(',') and look_comma:
            if "że" in element[:3] or "któr" in element[:5]:
                element = ", " + element
            else:
                element = " " + element
        return element

    def generate(self):
        return self._element('intro', False) + self._element('subject') + self._element('action') + self._element('action2') + self._element('motivation') + self._element('conclusion')


def main(argv):
    count = 1

    try:
        opts, args = getopt.getopt(argv, "c:", ["count="])
    except getopt.GetoptError:
        print("Argument error!")
        sys.exit(2)
    for o, a in opts:
        if o in ("-c", "--count"):
            count = int(a)
    k = Korwinator()
    for _ in range(count):
        print(k.generate())

if __name__ == "__main__":
    main(sys.argv[1:])