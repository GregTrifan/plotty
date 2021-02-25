from matplotlib import pyplot as plt
years = [1999,2000,2001,2002,2003]
price = [100,230,424,542,345]
def render():
    with plt.style.context('dark_background'):
        plt.plot(years,price,color="blue",marker='o')
    plt.title("Price evolution")
    plt.ylabel("$")
    plt.show()
render()