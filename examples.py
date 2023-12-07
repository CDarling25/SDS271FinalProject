from api import *

def main():
    
    example1 = BLS("food")
    example1.set_interest_Series()
    example1.get_request(2013, 2014)
    example1.summary_stats()
    example1.visualizer()

    recreation = BLS("Recreation")
    recreation.get_request(1999, 2000, ["CUUR0000SAR"])
    recreation.summary_stats()
    recreation.visualizer()

    medical = BLS("Medical")
    medical.set_interest_Series()
    medical.get_request(2000, 2014)
    medical.summary_stats()
    medical.visualizer()

if __name__ == "__main__":
    main()