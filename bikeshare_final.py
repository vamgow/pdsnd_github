"""
from google.colab import drive
drive.mount('/content/drive')

"""

import pandas as pd
import time

"""
chicago_csv = '/content/drive/My Drive/Bike Share/chicago.csv'
new_york_city_csv = '/content/drive/My Drive/Bike Share/new_york_city.csv'
washington_csv = '/content/drive/My Drive/Bike Share/washington.csv'
#df = pd.read_csv(chicago_csv)

"""




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




def get_filters():

  """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
  print("Hello! Let\'s explore some US bikeshare data!")




  while True:
    city = input("Which city would you like to see the data for?").lower()
    if city in ('new york city', 'washington', 'chicago'):
      break
    else:
      print("Invalid Input")





  month = 'all'
  day = 'all'
  while True:

    time_frame = input("Would you like to filter the data by month, day or none?").lower()
    if time_frame == 'month':

      while True:

        month = input("Which month data would you like to look at ?").lower()
        if month in ('january','february','march','april','may','june'):
          break
        else:
          print("Please input the fullname of the month")
      break

    elif time_frame == 'day':
      while True:
        day = int(input('which day? Please type your response as an integer (e.g, 1 = Monday..,7 = Sunday)'))
        days = [1,2,3,4,5,6,7]
        if day in days:
          break
        else:
          print("Invalid response. Please enter integer values from 1 to 7")
      break

    elif time_frame == 'none':
      break

    else:
      print("Invalid input. Please enter day, month or none")




  print('-'*40)
  return city, month, day


def load_data(city, month, day):




   # load data file into a dataframe
  df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
  df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
  df['month'] = df['Start Time'].dt.month
  df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
  if month != 'all':
     # use the index of the months list to get the corresponding int
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     month = months.index(month) + 1

  # filter by month to create the new dataframe
     df = df[df['month'] == month]

  # filter by day of week if applicable
  if day != 'all':




    # filter by day of week to create the new dataframe
    days = [1,2,3,4,5,6,7]
    day =  days.index(day)
    df = df[df['day_of_week'] == day]
  return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip

    df['Start End'] = df['Start Station'] + ' to '+df['End Station']
    frequent_route = df['Start End'].mode()[0]

    print("The most common start station is :", common_start)
    print("The most common end station is:",common_end)
    print("The most used route is", frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    common_month = df['month'].mode()[0]


    # display the most common day of week
    df['week'] = df['Start Time'].dt.day_name()
    common_week_day = df['week'].mode()[0]

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("The most common month is:",common_month)
    print("The most common day of the week is:",common_week_day)
    print("The most common hour is",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()



    # display mean travel time
    mean_duration = df['Trip Duration'].mean()

    print("The total travel time is {} minutes".format(total_duration))
    print("The mean travel time is:{}".format(mean_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    various_users = df['User Type'].value_counts()
    print("\n The count of the user group:\n {}".format(various_users))

    # Display counts of gender
    try:
      gender_count = df['Gender'].value_counts()
      # Display earliest, most recent, and most common year of birth
      oldest_biker = df['Birth Year'].min()
      youngest_biker = df['Birth Year'].max()
      common_birthyear = df['Birth Year'].mode()[0]
      print("\n The oldest birth year is {}".format(oldest_biker))
      print("\n The latest birth year is {}".format(youngest_biker))
      print("\n The most common birth year is {}".format(common_birthyear))
      print("\n The number of male and female users: \n {}".format(gender_count))
    except:
      print("No gender details available for Washington City")
      print("No Year of Birth details available for Washington City")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        count = 5
        while True:
            additional_data = input("Would you like to see the individual trip data:").lower()
            if additional_data != 'yes':
                break

            elif additional_data == 'yes':
                individual_data = df.iloc[:count]
                print(individual_data)
                while True:
                    more_data = input("would you like to see more data:").lower()
                    if more_data == 'yes':
                        count += 5
                        individual_data = df.iloc[:count]
                        print(individual_data)

                    elif more_data == 'no':
                        break

                    else:
                        print("Please check your typo:")
                break


            else:
                print("Please rectify your response.")









        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
