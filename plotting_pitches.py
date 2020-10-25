import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import sys


def plot_pitch(length, width, unity, linecolor, ax=None):
    """
    Function that plots a horizontal pitch - inspired by FCPython
    :param length: length of pitch
    :param width: width of pitch
    :param unity: units of measurements length + width
    :param linecolor: colors of lines on pitch
    :return: ax
    """
    if ax is None:
        ax = plt.gca()
    # Set unity
    if unity == "meters":
        try:
            assert length <= 120.5
            assert width <= 75.5
        except AssertionError:
            print("You've entered the wrong pitch dimensions - try again")
            sys.exit()

        # fig = plt.figure()
        # ax = fig.add_subplot(1, 1, 1)

        # Pitch Outline & Centre Line
        plt.plot([0, 0], [0, width], color=linecolor)
        plt.plot([0, length], [width, width], color=linecolor)
        plt.plot([length, length], [width, 0], color=linecolor)
        plt.plot([length, 0], [0, 0], color=linecolor)
        plt.plot([length / 2, length / 2], [0, width], color=linecolor)

        # Left Penalty Area
        plt.plot([16.5, 16.5], [(width / 2 + 16.5), (width / 2 - 16.5)], color=linecolor)
        plt.plot([0, 16.5], [(width / 2 + 16.5), (width / 2 + 16.5)], color=linecolor)
        plt.plot([16.5, 0], [(width / 2 - 16.5), (width / 2 - 16.5)], color=linecolor)

        # Right Penalty Area
        plt.plot([(length - 16.5), length], [(width / 2 + 16.5), (width / 2 + 16.5)], color=linecolor)
        plt.plot([(length - 16.5), (length - 16.5)], [(width / 2 + 16.5), (width / 2 - 16.5)], color=linecolor)
        plt.plot([(length - 16.5), length], [(width / 2 - 16.5), (width / 2 - 16.5)], color=linecolor)

        # Left 5-meters Box
        plt.plot([0, 5.5], [(width / 2 + 7.32 / 2 + 5.5), (width / 2 + 7.32 / 2 + 5.5)], color=linecolor)
        plt.plot([5.5, 5.5], [(width / 2 + 7.32 / 2 + 5.5), (width / 2 - 7.32 / 2 - 5.5)], color=linecolor)
        plt.plot([5.5, 0.5], [(width / 2 - 7.32 / 2 - 5.5), (width / 2 - 7.32 / 2 - 5.5)], color=linecolor)

        # Right 5 -eters Box
        plt.plot([length, length - 5.5], [(width / 2 + 7.32 / 2 + 5.5), (width / 2 + 7.32 / 2 + 5.5)],
                 color=linecolor)
        plt.plot([length - 5.5, length - 5.5], [(width / 2 + 7.32 / 2 + 5.5), width / 2 - 7.32 / 2 - 5.5],
                 color=linecolor)
        plt.plot([length - 5.5, length], [width / 2 - 7.32 / 2 - 5.5, width / 2 - 7.32 / 2 - 5.5], color=linecolor)

        # Prepare Circles
        centreCircle = plt.Circle((length / 2, width / 2), 9.15, color=linecolor, fill=False)
        centreSpot = plt.Circle((length / 2, width / 2), 0.8, color=linecolor)
        leftPenSpot = plt.Circle((11, width / 2), 0.8, color=linecolor)
        rightPenSpot = plt.Circle((length - 11, width / 2), 0.8, color=linecolor)

        # Draw Circles
        ax.add_patch(centreCircle)
        ax.add_patch(centreSpot)
        ax.add_patch(leftPenSpot)
        ax.add_patch(rightPenSpot)

        # Prepare Arcs
        leftArc = Arc((11, width / 2), height=18.3, width=18.3, angle=0, theta1=308, theta2=52, color=linecolor)
        rightArc = Arc((length - 11, width / 2), height=18.3, width=18.3, angle=0, theta1=128, theta2=232,
                       color=linecolor)

        # Draw Arcs
        ax.add_patch(leftArc)
        ax.add_patch(rightArc)
        # Axis titles

    # check unity again
    elif unity == "yards":
        # check boundaries again
        try:
            assert length <= 131
            assert width <= 101
        except AssertionError:
            print("You've entered the wrong pitch dimensions - try again")
            sys.exit()
        else:
            # # Create figure
            # fig = plt.figure()
            # # fig.set_size_inches(7, 5)
            # ax = fig.add_subplot(1, 1, 1)

            # Pitch Outline & Centre Line
            plt.plot([0, 0], [0, width], color=linecolor)
            plt.plot([0, length], [width, width], color=linecolor)
            plt.plot([length, length], [width, 0], color=linecolor)
            plt.plot([length, 0], [0, 0], color=linecolor)
            plt.plot([length / 2, length / 2], [0, width], color=linecolor)

            # Left Penalty Area
            plt.plot([18, 18], [(width / 2 + 18), (width / 2 - 18)], color=linecolor)
            plt.plot([0, 18], [(width / 2 + 18), (width / 2 + 18)], color=linecolor)
            plt.plot([18, 0], [(width / 2 - 18), (width / 2 - 18)], color=linecolor)

            # Right Penalty Area
            plt.plot([(length - 18), length], [(width / 2 + 18), (width / 2 + 18)], color=linecolor)
            plt.plot([(length - 18), (length - 18)], [(width / 2 + 18), (width / 2 - 18)], color=linecolor)
            plt.plot([(length - 18), length], [(width / 2 - 18), (width / 2 - 18)], color=linecolor)

            # Left 6-yard Box
            plt.plot([0, 6], [(width / 2 + 7.32 / 2 + 6), (width / 2 + 7.32 / 2 + 6)], color=linecolor)
            plt.plot([6, 6], [(width / 2 + 7.32 / 2 + 6), (width / 2 - 7.32 / 2 - 6)], color=linecolor)
            plt.plot([6, 0], [(width / 2 - 7.32 / 2 - 6), (width / 2 - 7.32 / 2 - 6)], color=linecolor)

            # Right 6-yard Box
            plt.plot([length, length - 6], [(width / 2 + 7.32 / 2 + 6), (width / 2 + 7.32 / 2 + 6)], color=linecolor)
            plt.plot([length - 6, length - 6], [(width / 2 + 7.32 / 2 + 6), width / 2 - 7.32 / 2 - 6], color=linecolor)
            plt.plot([length - 6, length], [(width / 2 - 7.32 / 2 - 6), width / 2 - 7.32 / 2 - 6], color=linecolor)

            # Prepare Circles; 10 yards distance. penalty on 12 yards
            centreCircle = plt.Circle((length / 2, width / 2), 10, color=linecolor, fill=False)
            centreSpot = plt.Circle((length / 2, width / 2), 0.8, color=linecolor)
            leftPenSpot = plt.Circle((12, width / 2), 0.8, color=linecolor)
            rightPenSpot = plt.Circle((length - 12, width / 2), 0.8, color=linecolor)

            # Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)

            # Prepare Arcs
            leftArc = Arc((11, width / 2), height=20, width=20, angle=0, theta1=312, theta2=48, color=linecolor)
            rightArc = Arc((length - 11, width / 2), height=20, width=20, angle=0, theta1=130, theta2=230,
                           color=linecolor)

            # Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)

    # Tidy Axes
    plt.axis('off')

    return ax


def plot_goal(linecolor='black'):
    """
    Function that plots only goal and surrounding area - Inspired by FCPython
    :param linecolor: colour of lines on pitch/goal
    :return: fig, ax
    """
    # Adopted from FC Python
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Pitch Outline & Centre Line
    plt.plot([0, 65], [0, 0], color=linecolor)
    plt.plot([65, 65], [50, 0], color=linecolor)
    plt.plot([0, 0], [50, 0], color=linecolor)

    # Left Penalty Area
    plt.plot([12.5, 52.5], [16.5, 16.5], color=linecolor)
    plt.plot([52.5, 52.5], [16.5, 0], color=linecolor)
    plt.plot([12.5, 12.5], [0, 16.5], color=linecolor)

    # Left 6-yard Box
    plt.plot([41.5, 41.5], [5.5, 0], color=linecolor)
    plt.plot([23.5, 41.5], [5.5, 5.5], color=linecolor)
    plt.plot([23.5, 23.5], [0, 5.5], color=linecolor)

    # Goal
    plt.plot([41.5 - 5.34, 41.5 - 5.34], [-2, 0], color=linecolor)
    plt.plot([23.5 + 5.34, 41.5 - 5.34], [-2, -2], color=linecolor)
    plt.plot([23.5 + 5.34, 23.5 + 5.34], [0, -2], color=linecolor)

    # Prepare Circles
    leftPenSpot = plt.Circle((65 / 2, 11), 0.8, color=linecolor)

    # Draw Circles
    ax.add_patch(leftPenSpot)

    # Prepare Arcs
    leftArc = Arc((32.5, 11), height=18.3, width=18.3, angle=0, theta1=38, theta2=142, color=linecolor)

    # Draw Arcs
    ax.add_patch(leftArc)

    # Tidy Axes
    plt.axis('off')

    return fig, ax


if __name__ == "__main__":
    plot_pitch(120, 80, 'yards', 'black')
    plot_goal()
    plt.show()