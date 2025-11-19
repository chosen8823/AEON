"""
Growth Canvas - The Visual Layer Where Code Blooms
No deletion, only growth. Watch your creation evolve like a living organism.
"""

import time
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


class GrowthPhase(Enum):
    """Stages of code evolution"""
    SEED = "seed"                    # Initial intention
    SPROUT = "sprout"                # First implementation
    GROWTH = "growth"                # Active development
    BLOOM = "bloom"                  # Feature complete
    FRUIT = "fruit"                  # Production ready
    WISDOM = "wisdom"                # Teaching others


class LayerType(Enum):
    """Different strata of code evolution"""
    FOUNDATION = "foundation"        # Core data structures
    LOGIC = "logic"                  # Business logic
    INTERFACE = "interface"          # UI/UX layer
    INTEGRATION = "integration"      # External connections
    INTELLIGENCE = "intelligence"    # AI/learning components


@dataclass
class CodeMolecule:
    """
    A single unit of creative code
    Like a DNA base pair - it contains meaning and can be inherited
    """
    id: str
    content: str                     # The actual code
    intention: str                   # What the creator wanted to achieve
    layer: LayerType
    phase: GrowthPhase
    timestamp: float
    parent_ids: List[str] = field(default_factory=list)
    children_ids: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    # Visual properties
    color: Tuple[int, int, int] = (100, 200, 150)  # RGB
    position: Tuple[float, float, float] = (0, 0, 0)  # 3D coordinates
    size: float = 1.0

    def evolve_to(self, new_phase: GrowthPhase):
        """Grow to the next phase"""
        self.phase = new_phase
        # Size increases with maturity
        phase_sizes = {
            GrowthPhase.SEED: 0.5,
            GrowthPhase.SPROUT: 0.8,
            GrowthPhase.GROWTH: 1.2,
            GrowthPhase.BLOOM: 1.5,
            GrowthPhase.FRUIT: 2.0,
            GrowthPhase.WISDOM: 2.5
        }
        self.size = phase_sizes.get(new_phase, 1.0)


@dataclass
class GrowthSnapshot:
    """A moment in time in the code's evolution"""
    timestamp: float
    molecules: List[CodeMolecule]
    harmony_score: float
    message: str  # What happened at this moment
    creator_note: Optional[str] = None


class GrowthCanvas:
    """
    The infinite canvas where code grows organically
    Students can zoom, scrub through time, and watch their creation evolve
    """

    def __init__(self, creator_name: str):
        self.creator_name = creator_name
        self.molecules = {}  # id -> CodeMolecule
        self.timeline = []  # List of GrowthSnapshots
        self.start_time = time.time()
        self.current_layer_focus = LayerType.FOUNDATION

    def plant_seed(self, intention: str, layer: LayerType = LayerType.FOUNDATION) -> CodeMolecule:
        """
        Plant the first seed of an idea
        This is where all creation begins
        """
        molecule_id = f"{layer.value}_{len(self.molecules)}_{time.time()}"

        molecule = CodeMolecule(
            id=molecule_id,
            content="# " + intention,  # Start as a comment
            intention=intention,
            layer=layer,
            phase=GrowthPhase.SEED,
            timestamp=time.time() - self.start_time,
            color=self._get_layer_color(layer),
            position=self._calculate_position(layer)
        )

        self.molecules[molecule_id] = molecule
        self._take_snapshot(f"Planted seed: {intention}")

        return molecule

    def grow_from(self,
                  parent_id: str,
                  new_content: str,
                  intention: str,
                  layer: Optional[LayerType] = None) -> CodeMolecule:
        """
        Grow new code from existing code
        This is ADDITIVE - the parent remains, the child grows from it
        """
        if parent_id not in self.molecules:
            raise ValueError(f"Parent molecule {parent_id} not found")

        parent = self.molecules[parent_id]
        layer = layer or parent.layer

        # Create child molecule
        child_id = f"{layer.value}_{len(self.molecules)}_{time.time()}"

        child = CodeMolecule(
            id=child_id,
            content=new_content,
            intention=intention,
            layer=layer,
            phase=GrowthPhase.SPROUT,
            timestamp=time.time() - self.start_time,
            parent_ids=[parent_id],
            color=self._get_layer_color(layer),
            position=self._calculate_child_position(parent)
        )

        # Link parent and child
        parent.children_ids.append(child_id)
        self.molecules[child_id] = child

        self._take_snapshot(f"Grew '{intention}' from '{parent.intention}'")

        return child

    def transform(self,
                  molecule_id: str,
                  new_content: str,
                  new_intention: str) -> CodeMolecule:
        """
        Transform existing code into something new
        The old version remains in history, a new branch grows
        """
        if molecule_id not in self.molecules:
            raise ValueError(f"Molecule {molecule_id} not found")

        original = self.molecules[molecule_id]

        # Create transformed version as a child
        return self.grow_from(
            parent_id=molecule_id,
            new_content=new_content,
            intention=f"Transformed: {new_intention}",
            layer=original.layer
        )

    def merge_branches(self,
                       molecule_ids: List[str],
                       merged_content: str,
                       intention: str,
                       layer: LayerType) -> CodeMolecule:
        """
        Merge multiple code branches into one
        All parents remain, the merged child grows from all of them
        """
        for mol_id in molecule_ids:
            if mol_id not in self.molecules:
                raise ValueError(f"Molecule {mol_id} not found")

        merge_id = f"{layer.value}_merge_{len(self.molecules)}_{time.time()}"

        merged = CodeMolecule(
            id=merge_id,
            content=merged_content,
            intention=intention,
            layer=layer,
            phase=GrowthPhase.GROWTH,
            timestamp=time.time() - self.start_time,
            parent_ids=list(molecule_ids),
            color=self._blend_colors([self.molecules[mid].color for mid in molecule_ids]),
            position=self._calculate_merge_position([self.molecules[mid] for mid in molecule_ids])
        )

        # Link all parents to this child
        for parent_id in molecule_ids:
            self.molecules[parent_id].children_ids.append(merge_id)

        self.molecules[merge_id] = merged
        self._take_snapshot(f"Merged {len(molecule_ids)} branches: {intention}")

        return merged

    def evolve_molecule(self, molecule_id: str, new_phase: GrowthPhase):
        """Advance a molecule to its next evolutionary phase"""
        if molecule_id not in self.molecules:
            raise ValueError(f"Molecule {molecule_id} not found")

        molecule = self.molecules[molecule_id]
        old_phase = molecule.phase
        molecule.evolve_to(new_phase)

        self._take_snapshot(f"Evolved '{molecule.intention}' from {old_phase.value} to {new_phase.value}")

    def time_scrub(self, moment: float) -> GrowthSnapshot:
        """
        Scrub through time to see the canvas at any moment
        Returns the closest snapshot to that time
        """
        if not self.timeline:
            return None

        # Find closest snapshot
        closest = min(self.timeline, key=lambda s: abs(s.timestamp - moment))
        return closest

    def get_genealogy(self, molecule_id: str) -> List[CodeMolecule]:
        """
        Get the full family tree of a molecule
        Trace back to the original seed
        """
        if molecule_id not in self.molecules:
            return []

        molecule = self.molecules[molecule_id]
        genealogy = [molecule]

        # Recursively get parents
        for parent_id in molecule.parent_ids:
            genealogy.extend(self.get_genealogy(parent_id))

        return genealogy

    def get_descendants(self, molecule_id: str) -> List[CodeMolecule]:
        """
        Get all children, grandchildren, etc. of a molecule
        See what grew from this seed
        """
        if molecule_id not in self.molecules:
            return []

        molecule = self.molecules[molecule_id]
        descendants = []

        for child_id in molecule.children_ids:
            descendants.append(self.molecules[child_id])
            descendants.extend(self.get_descendants(child_id))

        return descendants

    def export_growth_story(self) -> str:
        """
        Export the entire growth journey as a narrative
        This becomes the student's portfolio piece
        """
        story = f"# Growth Story of {self.creator_name}\n\n"
        story += f"Created: {datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')}\n"
        story += f"Total Molecules: {len(self.molecules)}\n"
        story += f"Timeline Snapshots: {len(self.timeline)}\n\n"

        story += "## Evolution Timeline\n\n"
        for snapshot in self.timeline:
            timestamp = datetime.fromtimestamp(self.start_time + snapshot.timestamp)
            story += f"**{timestamp.strftime('%H:%M:%S')}** - {snapshot.message}\n"
            if snapshot.creator_note:
                story += f"  _Note: {snapshot.creator_note}_\n"
            story += f"  Harmony: {snapshot.harmony_score:.2%}\n\n"

        return story

    def _take_snapshot(self, message: str, creator_note: Optional[str] = None):
        """Capture current state of the canvas"""
        snapshot = GrowthSnapshot(
            timestamp=time.time() - self.start_time,
            molecules=list(self.molecules.values()),
            harmony_score=self._calculate_harmony(),
            message=message,
            creator_note=creator_note
        )
        self.timeline.append(snapshot)

    def _calculate_harmony(self) -> float:
        """
        Calculate how harmonious the current state is
        More evolved molecules = higher harmony
        """
        if not self.molecules:
            return 1.0

        phase_values = {
            GrowthPhase.SEED: 0.2,
            GrowthPhase.SPROUT: 0.4,
            GrowthPhase.GROWTH: 0.6,
            GrowthPhase.BLOOM: 0.8,
            GrowthPhase.FRUIT: 0.95,
            GrowthPhase.WISDOM: 1.0
        }

        total_harmony = sum(phase_values[m.phase] for m in self.molecules.values())
        return total_harmony / len(self.molecules)

    def _get_layer_color(self, layer: LayerType) -> Tuple[int, int, int]:
        """Map layers to colors (bass to treble, dark to bright)"""
        colors = {
            LayerType.FOUNDATION: (80, 60, 100),      # Deep purple
            LayerType.LOGIC: (100, 150, 180),         # Blue
            LayerType.INTERFACE: (150, 200, 150),     # Green
            LayerType.INTEGRATION: (200, 180, 100),   # Yellow
            LayerType.INTELLIGENCE: (255, 200, 255)   # Bright magenta
        }
        return colors.get(layer, (128, 128, 128))

    def _calculate_position(self, layer: LayerType) -> Tuple[float, float, float]:
        """Calculate 3D position based on layer"""
        # Layers stack vertically (Y axis)
        y_positions = {
            LayerType.FOUNDATION: 0.0,
            LayerType.LOGIC: 1.0,
            LayerType.INTERFACE: 2.0,
            LayerType.INTEGRATION: 3.0,
            LayerType.INTELLIGENCE: 4.0
        }

        return (0.0, y_positions.get(layer, 0.0), 0.0)

    def _calculate_child_position(self, parent: CodeMolecule) -> Tuple[float, float, float]:
        """Position child near parent but slightly offset"""
        offset = len(parent.children_ids) * 0.5
        return (
            parent.position[0] + offset,
            parent.position[1],
            parent.position[2] + offset
        )

    def _calculate_merge_position(self, parents: List[CodeMolecule]) -> Tuple[float, float, float]:
        """Position merged molecule at center of parents"""
        avg_x = sum(p.position[0] for p in parents) / len(parents)
        avg_y = sum(p.position[1] for p in parents) / len(parents)
        avg_z = sum(p.position[2] for p in parents) / len(parents)
        return (avg_x, avg_y, avg_z)

    def _blend_colors(self, colors: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        """Blend multiple RGB colors"""
        avg_r = sum(c[0] for c in colors) // len(colors)
        avg_g = sum(c[1] for c in colors) // len(colors)
        avg_b = sum(c[2] for c in colors) // len(colors)
        return (avg_r, avg_g, avg_b)

    def __repr__(self):
        return f"<GrowthCanvas: {len(self.molecules)} molecules, {len(self.timeline)} snapshots, harmony={self._calculate_harmony():.2%}>"
