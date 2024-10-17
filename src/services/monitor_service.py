class MonitorService:
    def __init__(self, audio_listener, chat_listener, screen_recorder, report_generator):
        self.audio_listener = audio_listener
        self.chat_listener = chat_listener
        self.screen_recorder = screen_recorder
        self.report_generator = report_generator

    def start_monitoring(self):
        self.audio_listener.listen_to_audio()
        self.chat_listener.monitor_chat()

    def stop_monitoring(self):
        self.audio_listener.stop()
        self.chat_listener.stop()
        self.report_generator.generate_report()

