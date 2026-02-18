import time
from datetime import date
from pathlib import Path

class Log:
    def __init__(self, file: str = 'log.log'):
        self.file = Path(file).resolve()
        self.tags = {
            'alert': '[ALERT]',
            'critical': '[CRITICAL]',
            'important': '[IMPORTANT]',
            'info': '[INFO]',
            'warning': '[WARNING]',
            'error': '[ERROR]',
            'var': '[VAR]'
        }

    def write(self, *args, type: str = 'info', addTime: bool = True) -> None:
        """
        Function to add logs in logs file definite in server config if logs are enabled.

        Args:
            type (str): Log type. 
                Choices:
                    alert: Show alert.
                    critical: Shows critical.
                    info: Shows information.
                    important: Show important information.
                    warning: Shows warning.
                    error: Shows error.
                    var: Show any type of information.
            
            addTime (bool): Add datetime tag at the end of line.
        """
        # Log time
        ts = time.time()

        # Open the file as file
        with open(self.file, 'a') as file:
            text = ''.join(str(a) for a in args)

            # If it needs time
            if addTime:
                local = time.localtime(ts)
                ms = int((ts % 1) * 100)
                formatedTime = time.strftime('%H:%M:%S', local) + f'.{ms:02}'
                text += ' '
                text += f'[{date.today()} {formatedTime}]'
                
            # Add tag to text
            file.write(f'{self.tags[type]} {text}' + '\n')