def count_smileys(arr):
    simley = 0 
    simley += arr.count(":~)")
    simley += arr.count(":)")
    simley += arr.count(":-)")
    simley += arr.count(";~)")
    simley += arr.count(";)")
    simley += arr.count(";-)")
    simley += arr.count(":~D")
    simley += arr.count(":D")
    simley += arr.count(":-D")
    simley += arr.count(";~D")
    simley += arr.count(";D")
    simley += arr.count(";-D")
    return simley