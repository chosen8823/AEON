"""
Symphony Engine - The Musical Heart of the Platform
Translates system events, code execution, and data flows into living music
"""

import time
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum


class InstrumentType(Enum):
    """Musical instruments mapped to different system components"""
    # Bass - Foundation and Data
    BASS_DRUM = "bass_drum"           # System heartbeat
    CONTRABASS = "contrabass"         # Database operations
    BASS_GUITAR = "bass_guitar"       # Data flows

    # Mid-Range - Logic and Processing
    PIANO = "piano"                   # Core logic
    GUITAR = "guitar"                 # Function calls
    BRASS = "brass"                   # API operations
    STRINGS = "strings"               # Background processes

    # Treble - Interface and Events
    VIOLIN = "violin"                 # User interactions
    FLUTE = "flute"                   # UI events
    BELLS = "bells"                   # Notifications
    SYNTHESIZER = "synthesizer"       # AI operations


class NoteEvent(Enum):
    """Musical events for different system states"""
    SUCCESS = "major_chord"
    ERROR = "dissonant_chord"
    WARNING = "minor_chord"
    INFO = "single_note"
    GROWTH = "ascending_arpeggio"
    COMPLETION = "perfect_cadence"


@dataclass
class MusicalNote:
    """A single note in the system symphony"""
    instrument: InstrumentType
    pitch: int  # MIDI note number (0-127)
    velocity: int  # Volume (0-127)
    duration: float  # Seconds
    timestamp: float
    event_type: NoteEvent
    metadata: Dict


class SymphonyEngine:
    """
    The core engine that transforms system events into musical compositions
    """

    def __init__(self):
        self.score = []  # The growing musical composition
        self.active_notes = {}  # Currently playing notes
        self.tempo = 120  # BPM
        self.start_time = time.time()

    def emit_note(self,
                  instrument: InstrumentType,
                  pitch: int,
                  velocity: int = 64,
                  duration: float = 0.5,
                  event_type: NoteEvent = NoteEvent.INFO,
                  metadata: Dict = None) -> MusicalNote:
        """
        Emit a musical note from a system event
        """
        note = MusicalNote(
            instrument=instrument,
            pitch=pitch,
            velocity=velocity,
            duration=duration,
            timestamp=time.time() - self.start_time,
            event_type=event_type,
            metadata=metadata or {}
        )

        self.score.append(note)
        return note

    def system_heartbeat(self):
        """The foundational pulse of the system - steady bass drum"""
        return self.emit_note(
            InstrumentType.BASS_DRUM,
            pitch=36,  # C1 - deep bass
            velocity=80,
            duration=0.1,
            event_type=NoteEvent.INFO,
            metadata={"type": "heartbeat"}
        )

    def database_query(self, operation: str, success: bool = True):
        """Database operations as deep contrabass notes"""
        pitch = 40 if success else 38  # E1 for success, D1 for failure
        event = NoteEvent.SUCCESS if success else NoteEvent.ERROR

        return self.emit_note(
            InstrumentType.CONTRABASS,
            pitch=pitch,
            velocity=70,
            duration=0.3,
            event_type=event,
            metadata={"operation": operation}
        )

    def user_interaction(self, action: str, intensity: int = 64):
        """User events as bright violin notes"""
        # Map intensity to pitch (higher intensity = higher pitch)
        pitch = 60 + (intensity % 24)  # C4 to B5 range

        return self.emit_note(
            InstrumentType.VIOLIN,
            pitch=pitch,
            velocity=intensity,
            duration=0.2,
            event_type=NoteEvent.INFO,
            metadata={"action": action}
        )

    def ai_operation(self, operation: str, complexity: int = 50):
        """AI operations as ethereal synthesizer"""
        # Complex operations = higher, more sustained notes
        pitch = 72 + (complexity % 12)  # C5 to B5
        duration = 0.5 + (complexity / 100)

        return self.emit_note(
            InstrumentType.SYNTHESIZER,
            pitch=pitch,
            velocity=60,
            duration=duration,
            event_type=NoteEvent.GROWTH,
            metadata={"operation": operation, "complexity": complexity}
        )

    def code_execution(self, function_name: str, success: bool = True):
        """Function execution as guitar chords"""
        base_pitch = 50  # D3
        event = NoteEvent.SUCCESS if success else NoteEvent.ERROR

        return self.emit_note(
            InstrumentType.GUITAR,
            pitch=base_pitch,
            velocity=75,
            duration=0.4,
            event_type=event,
            metadata={"function": function_name}
        )

    def error_occurred(self, error_type: str, severity: int = 50):
        """Errors as dissonant chords that resolve through learning"""
        # Higher severity = more dissonant (lower pitch)
        pitch = 45 - (severity // 10)

        return self.emit_note(
            InstrumentType.BRASS,
            pitch=pitch,
            velocity=90,
            duration=0.6,
            event_type=NoteEvent.ERROR,
            metadata={"error": error_type, "severity": severity}
        )

    def growth_moment(self, achievement: str, magnitude: int = 50):
        """Learning breakthroughs as ascending arpeggios"""
        # Create a series of ascending notes
        notes = []
        base_pitch = 60  # C4

        for i in range(4):  # 4-note arpeggio
            pitch = base_pitch + (i * 4)  # Major 7th arpeggio
            note = self.emit_note(
                InstrumentType.BELLS,
                pitch=pitch,
                velocity=magnitude,
                duration=0.15,
                event_type=NoteEvent.GROWTH,
                metadata={"achievement": achievement, "step": i}
            )
            notes.append(note)

        return notes

    def completion_cadence(self, task: str):
        """Task completion as perfect cadence (V-I)"""
        # Dominant chord (V)
        v_chord = self.emit_note(
            InstrumentType.PIANO,
            pitch=67,  # G4
            velocity=80,
            duration=0.5,
            event_type=NoteEvent.COMPLETION,
            metadata={"task": task, "chord": "V"}
        )

        # Tonic chord (I) - resolution
        i_chord = self.emit_note(
            InstrumentType.PIANO,
            pitch=60,  # C4
            velocity=90,
            duration=1.0,
            event_type=NoteEvent.COMPLETION,
            metadata={"task": task, "chord": "I"}
        )

        return [v_chord, i_chord]

    def get_harmony_score(self) -> float:
        """
        Analyze the recent musical score to determine system health
        More harmony = healthier system
        Returns: 0.0 to 1.0 (1.0 = perfect harmony)
        """
        if not self.score:
            return 1.0

        recent_notes = self.score[-100:]  # Last 100 notes

        # Count successes vs errors
        successes = sum(1 for note in recent_notes if note.event_type == NoteEvent.SUCCESS)
        errors = sum(1 for note in recent_notes if note.event_type == NoteEvent.ERROR)
        growth = sum(1 for note in recent_notes if note.event_type == NoteEvent.GROWTH)

        total = len(recent_notes)

        # Calculate harmony score
        harmony = (successes + growth * 2) / (total + errors * 3)

        return min(1.0, harmony)

    def export_symphony(self, format: str = "midi") -> bytes:
        """
        Export the system symphony to playable format
        TODO: Implement MIDI export
        """
        # Placeholder for MIDI export
        return b"SYMPHONY_DATA"

    def __repr__(self):
        harmony = self.get_harmony_score()
        return f"<SymphonyEngine: {len(self.score)} notes, harmony={harmony:.2%}>"
