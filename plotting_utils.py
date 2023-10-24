def split_y_plot(df, col_x:str, col_y_1:str, col_y_2:str, x_rotation:int=0):
    """
    Create a dual-y axis plot to visualize two sets of data against a common x-axis.

    Parameters:
    - df (pandas DataFrame): The DataFrame containing the data to be plotted.
    - col_x (str): The name of the DataFrame column to be used as the x-axis values.
    - col_y_1 (str): The name of the first DataFrame column to be plotted on the left y-axis.
    - col_y_2 (str): The name of the second DataFrame column to be plotted on the right y-axis.
    - x_rotation (int, optional): The rotation angle for x-axis labels (default is 0).

    Returns:
    - None: The function displays the dual-y axis plot but does not return any value.

    Usage:
    - split_y_plot(data_frame, 'X-Column', 'Y1-Column', 'Y2-Column', x_rotation=45)

    Example:
    - split_y_plot(df, 'Date', 'Temperature', 'Humidity', x_rotation=45)

    Note:
    - The function uses Matplotlib to create the dual-y axis plot, allowing for easy comparison of two different datasets.
    - The x-axis represents 'col_x', and the left and right y-axes represent 'col_y_1' and 'col_y_2', respectively.
    - You can specify the rotation angle for x-axis labels with the 'x_rotation' parameter (default is 0).
    - The plot includes legends for both y-axes to distinguish the two datasets.

    Dependencies:
    - Ensure you have the 'pandas' and 'matplotlib' libraries installed to use this function.

    TODO: 
    - Add more control for 
        - color 
        - line-types 
        - labeling
    - Add ability to np.log series
    - tilt x-axis lables
    """

    fig, ax1 = plt.subplots()

    ax1.plot(df[col_x], df[col_y_1], label=col_y_1, color='blue')
    ax1.set_xlabel(col_x.replace('_', ' '))
    ax1.xticks(rotation=x_rotation)
    ax1.set_ylabel(col_y_1.replace('_', ' '), color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    
    ax2.plot(df[col_x], df[col_y_2], label=col_y_2, color='green')
    ax2.set_ylabel(col_y_2.replace('_', ' '), color='g')
    ax2.tick_params('y', colors='g')
    
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    # ax2.legend(lines + lines2, labels + labels2, loc='upper right')

    # plt.title(f"Plot with {col_y_1} & {col_y_2}")
    plt.show()