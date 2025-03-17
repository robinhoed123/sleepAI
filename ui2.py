import customtkinter as ctk
import pygame

# Initialize sound effects
pygame.mixer.init()
try:
    hover_sound = pygame.mixer.Sound("hover.mp3")
except:
    hover_sound = pygame.mixer.Sound(buffer=bytearray([0]))

# Set appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LifeStyleAI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Life Style AI")
        self.attributes('-fullscreen', False)
        
        # Start with main screen
        self.create_main_screen()
    
    def create_main_screen(self):
        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        # Add padding
        padding_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        padding_frame.pack(pady=10)
        
        # Title
        title = ctk.CTkLabel(self.main_frame, text="Life Style AI", font=("Arial", 60, "bold"))
        title.pack(pady=40)
        
        # Test AI button
        test_ai_button = self.create_button(self.main_frame, "Test AI", self.create_test_ai_screen, font_size=24, width=400, height=70)
        test_ai_button.pack(pady=30)
        
        # Visualize button
        visualize_button = self.create_button(self.main_frame, "Visualize", self.create_visualize_screen, font_size=24, width=400, height=70)
        visualize_button.pack(pady=30)
        
        # Exit button
        exit_button = self.create_button(self.main_frame, "Exit", self.destroy, font_size=24, width=400, height=70)
        exit_button.pack(pady=30)
    
    def create_test_ai_screen(self):
        # Clear main frame
        self.main_frame.destroy()
        
        # Create test AI frame
        self.test_ai_frame = ctk.CTkFrame(self)
        self.test_ai_frame.pack(fill="both", expand=True)
        
        # Title
        title = ctk.CTkLabel(self.test_ai_frame, text="Test AI", font=("Arial", 50, "bold"))
        title.pack(pady=(50, 40))
        
        # Create form frame - make it more compact horizontally
        form_frame = ctk.CTkFrame(self.test_ai_frame, width=600)
        form_frame = ctk.CTkFrame(self.test_ai_frame)
        form_frame.pack(pady=20, padx=100, fill="y")
        
        # Age
        age_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        age_frame.pack(pady=10, fill="x")
        
        age_label = ctk.CTkLabel(age_frame, text="Age:", font=("Arial", 18))
        age_label.pack(side="left", padx=20)
        
        self.age_var = ctk.StringVar(value="30")
        age_entry = ctk.CTkEntry(age_frame, textvariable=self.age_var, width=100, font=("Arial", 18))
        age_entry.pack(side="right", padx=20)
        # Add validation
        age_entry.bind("<FocusOut>", lambda event: self.validate_input(self.age_var, 1, 99))
        
        # Gender
        gender_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        gender_frame.pack(pady=10, fill="x")
        
        gender_label = ctk.CTkLabel(gender_frame, text="Gender:", font=("Arial", 18))
        gender_label.pack(side="left", padx=20)
        
        self.gender_var = ctk.StringVar(value="Male")
        gender_dropdown = ctk.CTkOptionMenu(gender_frame, variable=self.gender_var, 
                                           values=["Male", "Female", "Other"],
                                           width=100, font=("Arial", 18))
        gender_dropdown.pack(side="right", padx=20)
        
        # Total Sleep
        sleep_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        sleep_frame.pack(pady=10, fill="x")
        
        sleep_label = ctk.CTkLabel(sleep_frame, text="Total Sleep (hours):", font=("Arial", 18))
        sleep_label.pack(side="left", padx=20)
        
        self.sleep_var = ctk.StringVar(value="8")
        sleep_entry = ctk.CTkEntry(sleep_frame, textvariable=self.sleep_var, width=100, font=("Arial", 18))
        sleep_entry.pack(side="right", padx=20)
        sleep_entry.bind("<FocusOut>", lambda event: self.validate_input(self.sleep_var, 1, 16))
        
        # Sleep Quality
        quality_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        quality_frame.pack(pady=10, fill="x")
        
        quality_label = ctk.CTkLabel(quality_frame, text="Sleep Quality:", font=("Arial", 18))
        quality_label.pack(side="left", padx=20)
        
        self.quality_var = ctk.StringVar(value="7")
        quality_entry = ctk.CTkEntry(quality_frame, textvariable=self.quality_var, width=100, font=("Arial", 18))
        quality_entry.pack(side="right", padx=20)
        quality_entry.bind("<FocusOut>", lambda event: self.validate_input(self.quality_var, 1, 10))

        
        # Exercise
        exercise_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        exercise_frame.pack(pady=10, fill="x")
        
        exercise_label = ctk.CTkLabel(exercise_frame, text="Exercise (minutes):", font=("Arial", 18))
        exercise_label.pack(side="left", padx=20)
        
        self.exercise_var = ctk.StringVar(value="30")
        exercise_entry = ctk.CTkEntry(exercise_frame, textvariable=self.exercise_var, width=100, font=("Arial", 18))
        exercise_entry.pack(side="right", padx=20)
        exercise_entry.bind("<FocusOut>", lambda event: self.validate_input(self.exercise_var, 5, 300))
        
        # Caffeine
        caffeine_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        caffeine_frame.pack(pady=10, fill="x")
        
        caffeine_label = ctk.CTkLabel(caffeine_frame, text="Caffeine Intake (mg):", font=("Arial", 18))
        caffeine_label.pack(side="left", padx=20)
        
        self.caffeine_var = ctk.StringVar(value="100")
        caffeine_entry = ctk.CTkEntry(caffeine_frame, textvariable=self.caffeine_var, width=100, font=("Arial", 18))
        caffeine_entry.pack(side="right", padx=20)
        caffeine_entry.bind("<FocusOut>", lambda event: self.validate_input(self.caffeine_var, 1, 1000))
        
        # Screen Time
        screen_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        screen_frame.pack(pady=10, fill="x")
        
        screen_label = ctk.CTkLabel(screen_frame, text="Screen Time Before Bed (minutes):", font=("Arial", 18))
        screen_label.pack(side="left", padx=20)
        
        self.screen_var = ctk.StringVar(value="60")
        screen_entry = ctk.CTkEntry(screen_frame, textvariable=self.screen_var, width=100, font=("Arial", 18))
        screen_entry.pack(side="right", padx=20)
        screen_entry.bind("<FocusOut>", lambda event: self.validate_input(self.screen_var, 1, 180))
        
        # Work Hours
        work_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        work_frame.pack(pady=10, fill="x")
        
        work_label = ctk.CTkLabel(work_frame, text="Work Hours:", font=("Arial", 18))
        work_label.pack(side="left", padx=20)
        
        self.work_var = ctk.StringVar(value="8")
        work_entry = ctk.CTkEntry(work_frame, textvariable=self.work_var, width=100, font=("Arial", 18))
        work_entry.pack(side="right", padx=20)
        work_entry.bind("<FocusOut>", lambda event: self.validate_input(self.work_var, 1, 16))
        
        # Calculate button
        calculate_button = self.create_button(self.test_ai_frame, "Calculate", self.show_results, font_size=24, width=400, height=70)
        calculate_button.pack(pady=20)

        # Results section - placeholders
        self.results_frame = ctk.CTkFrame(self.test_ai_frame)
        self.results_frame.pack(pady=10)
        
        # Create placeholder results initially
        self.show_results()
        
        # Back button
        back_button = self.create_button(self.test_ai_frame, "Back to Main Screen", self.return_to_main, font_size=24, width=400, height=70)
        back_button.pack(pady=20)
    
    def create_visualize_screen(self):
        # Clear main frame
        self.main_frame.destroy()
        
        # Create visualize frame
        self.visualize_frame = ctk.CTkFrame(self)
        self.visualize_frame.pack(fill="both", expand=True)
        
        # Title
        title = ctk.CTkLabel(self.visualize_frame, text="Visualization", font=("Arial", 50, "bold"))
        title.pack(pady=(50, 40))
        
        # Just 3 placeholder buttons
        placeholder1 = self.create_button(self.visualize_frame, "Placeholder 1", 
                                         lambda: None, font_size=24, width=400, height=70)
        placeholder1.pack(pady=30)
        
        placeholder2 = self.create_button(self.visualize_frame, "Placeholder 2", 
                                         lambda: None, font_size=24, width=400, height=70)
        placeholder2.pack(pady=30)
        
        placeholder3 = self.create_button(self.visualize_frame, "Placeholder 3", 
                                         lambda: None, font_size=24, width=400, height=70)
        placeholder3.pack(pady=30)
        
        # Back button
        back_button = self.create_button(self.visualize_frame, "Back to Main Screen", 
                                        self.return_to_main, font_size=24, width=400, height=70)
        back_button.pack(pady=30)
    
    def create_button(self, parent, text, command, font_size=16, width=300, height=50):
        """Create custom buttons with hover effect"""
        button = ctk.CTkButton(
            parent, 
            text=text, 
            command=command,
            font=("Arial", font_size),
            width=width,
            height=height,
            corner_radius=10
        )
        
        # Add hover effect
        button.bind("<Enter>", lambda event: self.on_button_hover(event, button, width, height))
        button.bind("<Leave>", lambda event: self.on_button_leave(event, button, width, height))
        
        return button
    
    def on_button_hover(self, event, button, width, height):
        # Play sound
        hover_sound.play()
        
        # Slightly enlarge button
        button.configure(width=width+20, height=height+10)
    
    def on_button_leave(self, event, button, width, height):
        # Revert to normal size
        button.configure(width=width, height=height)
    
    def validate_input(self, var, min_val, max_val):
        """Validate numeric input within range"""
        try:
            value = int(var.get())
            if value < min_val:
                var.set(str(min_val))
            elif value > max_val:
                var.set(str(max_val))
        except ValueError:
            var.set(str(min_val))  # Default to min if not a valid number
    
    def show_results(self):
        """Display placeholder results"""
        # Clear previous results if any
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Create result labels with larger font
        font_size = 18
        
        # Productivity score
        productivity_frame = ctk.CTkFrame(self.results_frame, fg_color="transparent")
        productivity_frame.pack(pady=10, fill="x")
        
        productivity_label = ctk.CTkLabel(productivity_frame, text="Productivity Score:", font=("Arial", font_size))
        productivity_label.pack(side="left", padx=20)
        
        productivity_result = ctk.CTkLabel(productivity_frame, text="7.5/10", font=("Arial", font_size, "bold"))
        productivity_result.pack(side="right", padx=20)
        
        # Mood score
        mood_frame = ctk.CTkFrame(self.results_frame, fg_color="transparent")
        mood_frame.pack(pady=10, fill="x")
        
        mood_label = ctk.CTkLabel(mood_frame, text="Mood Score:", font=("Arial", font_size))
        mood_label.pack(side="left", padx=20)
        
        mood_result = ctk.CTkLabel(mood_frame, text="8.2/10", font=("Arial", font_size, "bold"))
        mood_result.pack(side="right", padx=20)
        
        # Stress level
        stress_frame = ctk.CTkFrame(self.results_frame, fg_color="transparent")
        stress_frame.pack(pady=10, fill="x")
        
        stress_label = ctk.CTkLabel(stress_frame, text="Stress Level:", font=("Arial", font_size))
        stress_label.pack(side="left", padx=20)
        
        stress_result = ctk.CTkLabel(stress_frame, text="5.4/10", font=("Arial", font_size, "bold"))
        stress_result.pack(side="right", padx=20)
        

        
    def return_to_main(self):
        """Return to main screen"""
        # Clear current frames
        if hasattr(self, 'test_ai_frame') and self.test_ai_frame:
            self.test_ai_frame.destroy()
            self.create_main_screen()
        if hasattr(self, 'visualize_frame') and self.visualize_frame:
            self.visualize_frame.destroy()
            self.create_main_screen()
if __name__ == "__main__":
    app = LifeStyleAI()
    app.mainloop()