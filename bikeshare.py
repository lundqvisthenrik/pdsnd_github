import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Input City:").lower()

    while city not in ['chicago','new york city','washington']:
        city = input("City name not valid. Try again!\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Input month:").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Input day:").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv("{}.csv".format(city.replace(" ","_")))

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])

    df['month']=df['Start Time'].apply(lambda x: x.month)
    df['dayofweek']=df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month != 'all':
        months = ['january','february','march','april','may','june','july','august','september','october','november','december']
        month = months.index(month)+1
        df=df.loc[df['month']==month,:]

    if day != 'all':
        df=df.loc[df['dayofweek']==day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month:{}".format(str(df['month'].mode().values[0])))

    # TO DO: display the most common day of week
    print("Most common day:{}".format(str(df['dayofweek'].mode().values[0])))

    # TO DO: display the most common start hour
    df['starthour']=df['Start Time'].dt.hour
    print("Most common hour:{}".format(str(df['starthour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station:{}".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("Most common end station:{}".format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combinations']=df['Start Station']+" "+df['End Station']
    print("Most frequent combination of start station and end station trip:{}".format(df['combinations'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['traveltime']=df['End Time']-df['Start Time']
    # TO DO: display total travel time
    print("Total travel time:{}".format(str(df['traveltime'].sum())))

    # TO DO: display mean travel time
    print("Mean travel time:{}".format(str(df['traveltime'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:

        print("Counts of gender:")
        print(df['Gender'].value_counts())
    else:
        print("Error")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest year of birth:{}".format(str(int(df['Birth Year'].min()))))
        print("Most recent year of birth:{}".format(str(int(df['Birth Year'].max()))))
        print("Most common year of birth:{}".format(str(int(df['Birth Year'].mode().values[0]))))
    else:
        print("Error")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):

    start_loc = 0
    end_loc = 5

    rawdata = input("See raw data?:").lower()

    if rawdata == 'yes':
        while end_loc <= df.shape[0]-1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            datacont = input("Continue?:").lower()
            if datacont == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
