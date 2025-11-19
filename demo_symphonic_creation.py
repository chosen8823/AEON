"""
Demo: Watch the Symphonic Platform in Action
This shows a student creating their first project - a simple web API
Watch the symphony play and the code grow!
"""

import time
from symphonic_platform.core.symphony_engine import SymphonyEngine, InstrumentType, NoteEvent
from symphonic_platform.core.growth_canvas import GrowthCanvas, LayerType, GrowthPhase


def demo_student_journey():
    """
    Simulate a student's creative journey
    Building a simple REST API while learning
    """

    print("=" * 60)
    print("🎵 SYMPHONIC PLATFORM DEMO 🎨")
    print("=" * 60)
    print("\nStudent: Sarah")
    print("Project: Building her first API\n")
    print("=" * 60)
    print()

    # Initialize the engines
    symphony = SymphonyEngine()
    canvas = GrowthCanvas(creator_name="Sarah")

    time.sleep(1)

    # PHASE 1: THE SEED - Student expresses intention
    print("\n📍 PHASE 1: PLANTING THE SEED")
    print("-" * 40)
    print("Sarah: 'I want to create an API that helps people track their habits'")

    seed = canvas.plant_seed(
        intention="Create a habit tracking API",
        layer=LayerType.FOUNDATION
    )

    # Symphony plays the beginning
    symphony.system_heartbeat()
    symphony.ai_operation("Processing student intention", complexity=30)

    print(f"✨ Seed planted: {seed.intention}")
    print(f"🎵 Harmony Score: {canvas._calculate_harmony():.2%}")
    time.sleep(1.5)

    # PHASE 2: FOUNDATION GROWS
    print("\n\n📍 PHASE 2: BUILDING FOUNDATION")
    print("-" * 40)
    print("Sarah: 'I need a database to store habit data'")

    db_code = canvas.grow_from(
        parent_id=seed.id,
        new_content="""
class HabitDatabase:
    def __init__(self):
        self.habits = {}
        self.user_progress = {}
    """,
        intention="Create database structure for habits",
        layer=LayerType.FOUNDATION
    )

    # Symphony reacts
    symphony.database_query("CREATE TABLE habits", success=True)
    symphony.code_execution("HabitDatabase.__init__", success=True)

    print(f"✨ Foundation growing...")
    print(f"   Created: {db_code.intention}")
    print(f"🎵 Symphony playing: Database operations (Contrabass)")
    print(f"🎨 Growth Phase: {db_code.phase.value}")
    time.sleep(1.5)

    # PHASE 3: LOGIC LAYER
    print("\n\n📍 PHASE 3: ADDING LOGIC")
    print("-" * 40)
    print("Sarah: 'Users need to add and complete habits'")

    logic_code = canvas.grow_from(
        parent_id=db_code.id,
        new_content="""
def add_habit(user_id, habit_name):
    habit_id = generate_id()
    habits[habit_id] = {
        'user_id': user_id,
        'name': habit_name,
        'created_at': now(),
        'streak': 0
    }
    return habit_id

def mark_complete(habit_id):
    habit = habits[habit_id]
    habit['streak'] += 1
    habit['last_completed'] = now()
    # Celebrate the streak!
    return habit['streak']
    """,
        intention="Implement core habit tracking logic",
        layer=LayerType.LOGIC
    )

    # Symphony plays mid-range instruments
    symphony.code_execution("add_habit", success=True)
    symphony.code_execution("mark_complete", success=True)
    symphony.user_interaction("Habit completed!", intensity=80)

    print(f"✨ Logic layer emerging...")
    print(f"   Created: {logic_code.intention}")
    print(f"🎵 Symphony playing: Function calls (Guitar)")
    canvas.evolve_molecule(logic_code.id, GrowthPhase.GROWTH)
    print(f"🎨 Evolved to: {logic_code.phase.value}")
    time.sleep(1.5)

    # PHASE 4: LEARNING MOMENT (AN ERROR!)
    print("\n\n📍 PHASE 4: LEARNING MOMENT")
    print("-" * 40)
    print("Sarah: 'Oh no! What if the habit doesn't exist?'")
    print("         (She forgot error handling)")

    # Symphony plays dissonance
    symphony.error_occurred("KeyError: habit not found", severity=40)

    print("🎵 Symphony: Dissonant chord (Error detected)")
    print("💡 Platform: 'This is beautiful! You've discovered error handling!'")

    # But errors are just growth opportunities!
    improved_logic = canvas.transform(
        molecule_id=logic_code.id,
        new_content="""
def mark_complete(habit_id):
    if habit_id not in habits:
        raise HabitNotFoundError(f"No habit with id {habit_id}")

    habit = habits[habit_id]
    habit['streak'] += 1
    habit['last_completed'] = now()
    return habit['streak']
    """,
        new_intention="Add error handling for invalid habits"
    )

    # Symphony resolves to harmony
    symphony.growth_moment("Learned error handling!", magnitude=70)

    print(f"✨ Growth through learning!")
    print(f"   Transformed into: {improved_logic.intention}")
    print(f"🎵 Symphony: Ascending arpeggio (Growth moment!)")
    canvas.evolve_molecule(improved_logic.id, GrowthPhase.BLOOM)
    time.sleep(2)

    # PHASE 5: INTERFACE LAYER
    print("\n\n📍 PHASE 5: CREATING THE INTERFACE")
    print("-" * 40)
    print("Sarah: 'Now I need API endpoints so people can use this!'")

    api_code = canvas.grow_from(
        parent_id=improved_logic.id,
        new_content="""
@app.route('/api/habits', methods=['POST'])
def create_habit():
    data = request.json
    habit_id = add_habit(data['user_id'], data['habit_name'])
    return {'habit_id': habit_id, 'message': 'Habit created!'}

@app.route('/api/habits/<id>/complete', methods=['POST'])
def complete_habit(id):
    streak = mark_complete(id)
    return {'streak': streak, 'message': f'Amazing! {streak} day streak!'}
    """,
        intention="Create REST API endpoints",
        layer=LayerType.INTERFACE
    )

    # Symphony plays bright treble instruments
    symphony.user_interaction("API endpoint created", intensity=90)
    symphony.code_execution("create_habit", success=True)

    print(f"✨ Interface blossoming...")
    print(f"   Created: {api_code.intention}")
    print(f"🎵 Symphony playing: User interactions (Violin)")
    canvas.evolve_molecule(api_code.id, GrowthPhase.FRUIT)
    print(f"🎨 Reached: {api_code.phase.value} - Production ready!")
    time.sleep(1.5)

    # PHASE 6: COMPLETION
    print("\n\n📍 PHASE 6: COMPLETION CADENCE")
    print("-" * 40)
    print("Sarah: 'It works! My first API is alive!'")

    # Perfect cadence - V to I
    symphony.completion_cadence("Habit Tracking API")

    print("🎵 Symphony: Perfect Cadence (V → I)")
    print("🎨 Canvas: All layers integrated and harmonious")
    print(f"🏆 Final Harmony Score: {canvas._calculate_harmony():.2%}")
    time.sleep(2)

    # SHOW THE GROWTH STORY
    print("\n\n" + "=" * 60)
    print("📖 SARAH'S GROWTH STORY")
    print("=" * 60)

    print(f"\nMolecules created: {len(canvas.molecules)}")
    print(f"Timeline snapshots: {len(canvas.timeline)}")
    print(f"Layers touched: {len(set(m.layer for m in canvas.molecules.values()))}")

    print("\n🌱 Evolution Path:")
    for snapshot in canvas.timeline:
        print(f"  {snapshot.timestamp:.1f}s - {snapshot.message}")

    # Show genealogy
    print("\n🧬 Code Genealogy (from seed to fruit):")
    final_molecule = api_code
    genealogy = canvas.get_genealogy(final_molecule.id)

    for i, molecule in enumerate(reversed(genealogy)):
        indent = "  " * i
        print(f"{indent}└─ {molecule.intention} [{molecule.phase.value}]")

    # Symphony stats
    print("\n🎵 Symphony Statistics:")
    print(f"   Total notes played: {len(symphony.score)}")
    print(f"   System harmony: {symphony.get_harmony_score():.2%}")

    note_types = {}
    for note in symphony.score:
        instrument = note.instrument.value
        note_types[instrument] = note_types.get(instrument, 0) + 1

    print(f"   Instruments used:")
    for instrument, count in sorted(note_types.items()):
        print(f"      {instrument}: {count} notes")

    print("\n" + "=" * 60)
    print("✨ CREATION COMPLETE ✨")
    print("=" * 60)
    print("\nThis is how students learn in the Symphonic Platform:")
    print("  • Every action creates music")
    print("  • Every line of code is a living organism")
    print("  • Mistakes become beautiful learning moments")
    print("  • The journey is visible, tangible, FELT")
    print("\nNo deletion. Only growth. Only ascension. 🌱🎵✨")
    print("=" * 60)


if __name__ == "__main__":
    demo_student_journey()
