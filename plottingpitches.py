import matplotlib.pyplot as plt


def plot_pitch(pitchcolour=None, linecolour=None, orientation=None, view=None):
    """
    Funciton to plot a football pitch in matplotlib

    Parameters
    ------------
    pitchcolour: string (colour name or hexcode), rgb array [a, b, c]
    linecolour: string (colour name or hexcode), rgb array [a, b, c]
    orientation: string (half or full)
    view: string (vertical or horizontal)

    Example
    ------------
    plotpitch(pitchcolour="#195905", linecolour="#faf0e6",
         orientation = "vertical", view = "half")
    """

    if orientation.lower().startswith("h"):
        if view.lower().startswith("h"):
            fig, ax = plt.subplots(figsize=(10.4, 6.8))
            plt.xlim(49, 105)
            plt.ylim(-1, 69)
        else:
            fig, ax = plt.subplots(figsize=(10.4, 6.8))
            plt.xlim(-1, 105)
            plt.ylim(-1, 69)
        ax.axis('off')

        # side and goal lines
        ly1 = [0, 0, 68, 68, 0]
        lx1 = [0, 104, 104, 0, 0]
        # zorder controls which elements are above others
        plt.plot(lx1, ly1, color=linecolour, zorder=5)

        # 18 yard boxes
        ly2 = [13.84, 13.84, 54.16, 54.16]
        lx2 = [104, 87.5, 87.5, 104]
        plt.plot(lx2, ly2, color=linecolour, zorder=5)

        ly3 = [13.84, 13.84, 54.16, 54.16]
        lx3 = [0, 16.5, 16.5, 0]
        plt.plot(lx3, ly3, color=linecolour, zorder=5)

        # Goals
        ly4 = [30.34, 30.34, 37.66, 37.66]
        lx4 = [104, 104.2, 104.2, 104]
        plt.plot(lx4, ly4, color=linecolour, zorder=5)

        ly5 = [30.34, 30.34, 37.66, 37.66]
        lx5 = [0, -0.2, -0.2, 0]
        plt.plot(lx5, ly5, color=linecolour, zorder=5)

        # 6 yard boxes
        ly6 = [24.84, 24.84, 43.16, 43.16]
        lx6 = [104, 99.5, 99.5, 104]
        plt.plot(lx6, ly6, color=linecolour, zorder=5)

        ly7 = [24.84, 24.84, 43.16, 43.16]
        lx7 = [0, 4.5, 4.5, 0]
        plt.plot(lx7, ly7, color=linecolour, zorder=5)

        # Halfway line
        ly8 = [0, 68]
        lx8 = [52, 52]
        plt.plot(lx8, ly8, color=linecolour, zorder=5)

        # Kick off and penalty spots
        plt.scatter(93, 34, color=linecolour, zorder=5)
        plt.scatter(11, 34, color=linecolour, zorder=5)
        plt.scatter(52, 34, color=linecolour, zorder=5)

        # Add centre circle and circles for curved line at edge of box
        circle1 = plt.Circle((93.5, 34), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=1, alpha=1)
        circle2 = plt.Circle((10.5, 34), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=1, alpha=1)
        circle3 = plt.Circle((52, 34), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=2, alpha=1)

        # Add rectangles to make curved line from circle1+2
        rec1 = plt.Rectangle((87.5, 20), 16, 30, ls="-",
                             color=pitchcolour, zorder=1, alpha=1)
        rec2 = plt.Rectangle((0, 20), 16.5, 30, ls="-",
                             color=pitchcolour, zorder=1, alpha=1)

        # Pitch rectangle
        rec3 = plt.Rectangle(
            (-1, -1), 106, 70, color=pitchcolour, zorder=1, alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)

    else:
        if view.lower().startswith("h"):
            fig, ax = plt.subplots(figsize=(10.4, 6.8))
            plt.ylim(49, 105)
            plt.xlim(-1, 69)
        else:
            fig, ax = plt.subplots(figsize=(6.8, 10.4))
            plt.ylim(-1, 105)
            plt.xlim(-1, 69)
        ax.axis('off')

        # side and goal lines
        lx1 = [0, 0, 68, 68, 0]
        ly1 = [0, 104, 104, 0, 0]
        # zorder controls which elements are above others
        plt.plot(lx1, ly1, color=linecolour, zorder=5)

        # 18 yard boxes
        lx2 = [13.84, 13.84, 54.16, 54.16]
        ly2 = [104, 87.5, 87.5, 104]
        plt.plot(lx2, ly2, color=linecolour, zorder=5)

        lx3 = [13.84, 13.84, 54.16, 54.16]
        ly3 = [0, 16.5, 16.5, 0]
        plt.plot(lx3, ly3, color=linecolour, zorder=5)

        # Goals
        lx4 = [30.34, 30.34, 37.66, 37.66]
        ly4 = [104, 104.2, 104.2, 104]
        plt.plot(lx4, ly4, color=linecolour, zorder=5)

        lx5 = [30.34, 30.34, 37.66, 37.66]
        ly5 = [0, -0.2, -0.2, 0]
        plt.plot(lx5, ly5, color=linecolour, zorder=5)

        # 6 yard boxes
        lx6 = [24.84, 24.84, 43.16, 43.16]
        ly6 = [104, 99.5, 99.5, 104]
        plt.plot(lx6, ly6, color=linecolour, zorder=5)

        lx7 = [24.84, 24.84, 43.16, 43.16]
        ly7 = [0, 4.5, 4.5, 0]
        plt.plot(lx7, ly7, color=linecolour, zorder=5)

        # Halfway line
        lx8 = [0, 68]
        ly8 = [52, 52]
        plt.plot(lx8, ly8, color=linecolour, zorder=5)

        # Kick off and penalty spots
        plt.scatter(34, 93, color=linecolour, zorder=5)
        plt.scatter(34, 11, color=linecolour, zorder=5)
        plt.scatter(34, 52, color=linecolour, zorder=5)

        # Add centre circle and circles for curved line at edge of box
        circle1 = plt.Circle((34, 93.5), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=1, alpha=1)
        circle2 = plt.Circle((34, 10.5), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=1, alpha=1)
        circle3 = plt.Circle((34, 52), 9.15, ls="solid", lw="1.5",
                             color=linecolour, fill=False, zorder=2, alpha=1)

        # Add rectangles to make curved line from circle1+2
        rec1 = plt.Rectangle((20, 87.5), 30, 16.5, ls="-",
                             color=pitchcolour, zorder=1, alpha=1)
        rec2 = plt.Rectangle((20, 0), 30, 16.5, ls="-",
                             color=pitchcolour, zorder=1, alpha=1)

        # Pitch rectangle
        rec3 = plt.Rectangle(
            (-1, -1), 70, 106, color=pitchcolour, zorder=1, alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        # plt.show()
