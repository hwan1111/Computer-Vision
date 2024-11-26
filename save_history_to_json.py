import json

def save_history_to_json(history, file_path):
    """
    모델 학습 히스토리를 JSON 파일로 저장하는 함수.

    Parameters:
    - history (keras.callbacks.History): model.fit()으로 반환된 학습 히스토리 객체.
    - file_path (str): 히스토리를 저장할 파일 경로.

    Returns:
    - None
    """
    try:
        # 히스토리 객체에서 딕셔너리 추출
        history_dict = history.history

        # JSON 파일로 저장
        with open(file_path, 'w') as json_file:
            json.dump(history_dict, json_file)
        
        print(f"History successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving history: {e}")
