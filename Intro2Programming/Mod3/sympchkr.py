#
def main():
    symptom=False
    positive_response=['y','Y','yes','Yes','YES']
    print(f'Enter Y or N for each statement')
    if input('Do you have a fever or chills? ') in positive_response:
        symptom=True
    elif input(f'Do you have a cough? ') in positive_response:
        symptom=True
    elif input(f'Do you have shortness of breath or difficulty breathing? ') in positive_response:
        symptom=True
    elif input(f'Do you have muscle or body aches? ') in positive_response:
        symptom=True
    elif input(f'Do you have a headache? ') in positive_response:
        symptom=True
    elif input(f'Do you have a loss of taste or smell? ') in positive_response:
        symptom=True
    elif input(f'Do you have a sore throat? ') in positive_response:
        symptom=True
    elif input(f'Do you have congestion or a runny nose? ') in positive_response:
        symptom=True
    elif input(f'Do you have nausea or vomiting? ') in positive_response:
        symptom=True
    elif input(f'Do you have diarrhea? ') in positive_response:
        symptom=True
    elif input(f'Can you confirm that you are not experiencing any symptoms? ') in positive_response:
        pass
    else:
        symptom=True
    if symptom:
        print(f'Please do not come to campus at this time.')
    elif input(f'Are you taking over-the-counter meds for cold or flu? ') in positive_response:
        print(f'Please do not come to campus at this time.')
    elif input(f'Have you tested positive for COVID and/or been advised to self-isolate? ') in positive_response:
        print(f'Please do not come to campus at this time.')
    else:
        print(f'You are okay to visit campus!')
if __name__=='__main__':
    main()
           
