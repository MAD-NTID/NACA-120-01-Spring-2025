def box():
    print("====================")
    print("||                ||")
    print("||                ||")
    print("||                ||")
    print("||                ||")
    print("||                ||")
    print("====================")

def hello_your_name(name):
    print("Hello your name is", name)

def main():
    box()

    # Honors DRY principles
    hello_your_name("Tony")
    hello_your_name("Shashank")
    hello_your_name("Aidan")

    # Violation of DRY (Don't Repeat Yourself) principles
    print("Hello your name is Tony")
    print("Hello your name is Shashank")
    print("Hello your name is Aidan")

main()