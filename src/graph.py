import matplotlib.pyplot as plt

def graphing(data, saveLocation):
    fig, ax = plt.subplots(figsize = (12,9))
    ax.plot(data["Reduced Position"], data["Reduced Phi"], label=r"$x(r)$")
    # ax.plot(data["Reduced Position"], data["Reduced Energy"], label=r"$\tilde{E}(r)$")
    # ax.plot(data["Reduced Position"], data["Reduced Charge"], label=r"$\tilde{Q}(r)$")
    ax.set_ylabel(r"$x(r), E(r), Q(r)$")
    ax.set_xlabel(r"$r$")
    ax.set_xlim()
    ax.set_ylim()
    plt.legend()
    plt.savefig(saveLocation)
    plt.close()