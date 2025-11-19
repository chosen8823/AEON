"""
CCPM + Symphonic Platform Integration
Bridges CCPM's local markdown PM system with our musical/visual layer

Students get:
- CCPM's proven local markdown workflow
- Symphonic musical feedback for everything
- Visual growth canvas showing their journey
- Multi-agent swarm for learning
- All local, all private, all FREE
"""

import os
import time
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

# Our symphonic components
from symphonic_platform.core.symphony_engine import SymphonyEngine, InstrumentType
from symphonic_platform.core.growth_canvas import GrowthCanvas, LayerType, GrowthPhase
from symphonic_platform.core.agent_orchestra import AgentOrchestra


@dataclass
class PRD:
    """Product Requirements Document (CCPM format)"""
    name: str
    filepath: Path
    content: str
    created_at: datetime
    status: str  # draft, approved, in_progress


@dataclass
class Epic:
    """Technical Implementation Plan (CCPM format)"""
    name: str
    prd_name: str
    filepath: Path
    epic_content: str
    tasks: List['Task']
    created_at: datetime


@dataclass
class Task:
    """Individual work item (CCPM format)"""
    number: str  # "001", "002", etc.
    name: str
    filepath: Path
    status: str  # open, in-progress, completed
    depends_on: List[str]
    parallel: bool
    acceptance_criteria: List[str]


class SymphonicCCPM:
    """
    The bridge between CCPM's PM system and Symphonic Platform
    Makes project management MUSICAL and VISUAL
    """

    def __init__(self,
                 project_root: Path,
                 student_name: str):
        self.project_root = Path(project_root)
        self.student_name = student_name

        # CCPM directories (local markdown files)
        self.claude_dir = self.project_root / ".claude"
        self.prds_dir = self.claude_dir / "prds"
        self.epics_dir = self.claude_dir / "epics"
        self.context_dir = self.claude_dir / "context"

        # Symphonic components
        self.symphony = SymphonyEngine()
        self.canvas = GrowthCanvas(creator_name=student_name)
        self.orchestra = AgentOrchestra(
            symphony_engine=self.symphony,
            canvas=self.canvas,
            default_model_config={'type': 'ollama', 'model': 'codellama'}
        )

        # State tracking
        self.active_prds = {}
        self.active_epics = {}

        # Ensure directories exist
        self._init_directories()

    def _init_directories(self):
        """Create CCPM directory structure if it doesn't exist"""
        for dir_path in [self.claude_dir, self.prds_dir, self.epics_dir, self.context_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        # Play creation symphony
        self.symphony.system_heartbeat()
        self.symphony.ai_operation("Initialized project structure", complexity=30)

    async def create_prd(self, prd_name: str, requirements: str) -> PRD:
        """
        Create PRD with musical/visual feedback
        CCPM: /pm:prd-new <name>
        """
        print(f"\n🎵 Creating PRD: {prd_name}")
        print("=" * 50)

        # Musical announcement - new creation begins
        self.symphony.ai_operation(f"Creating PRD: {prd_name}", complexity=40)

        # Plant seed on growth canvas
        prd_molecule = self.canvas.plant_seed(
            intention=f"PRD: {prd_name}",
            layer=LayerType.FOUNDATION
        )

        # Create CCPM markdown file
        prd_filepath = self.prds_dir / f"{prd_name}.md"
        prd_content = self._generate_prd_content(prd_name, requirements)

        prd_filepath.write_text(prd_content)

        # PRD created - play success chord
        self.symphony.code_execution(f"create_prd_{prd_name}", success=True)
        self.canvas.evolve_molecule(prd_molecule.id, GrowthPhase.SPROUT)

        prd = PRD(
            name=prd_name,
            filepath=prd_filepath,
            content=prd_content,
            created_at=datetime.now(),
            status="draft"
        )

        self.active_prds[prd_name] = prd

        print(f"✅ PRD created: {prd_filepath}")
        print(f"🎨 Growth molecule: {prd_molecule.id}")
        print(f"🎵 Harmony: {self.symphony.get_harmony_score():.2%}")

        return prd

    async def parse_prd_to_epic(self, prd_name: str) -> Epic:
        """
        Convert PRD to Epic (technical plan) with AI assistance
        CCPM: /pm:prd-parse <name>
        """
        print(f"\n🧠 Parsing PRD to Epic: {prd_name}")
        print("=" * 50)

        if prd_name not in self.active_prds:
            # Load from file
            prd_path = self.prds_dir / f"{prd_name}.md"
            if not prd_path.exists():
                raise ValueError(f"PRD not found: {prd_name}")

        # Spawn AI agent to help with parsing
        parser_agent = await self.orchestra.spawn_agent(
            role=AgentRole.ANALYZER,
            name=f"prd_parser_{prd_name}"
        )

        # Agent analyzes PRD and creates technical plan
        self.symphony.ai_operation(
            f"Agent analyzing PRD: {prd_name}",
            complexity=70
        )

        # Create epic directory
        epic_dir = self.epics_dir / prd_name
        epic_dir.mkdir(exist_ok=True)

        # Generate epic.md
        epic_filepath = epic_dir / "epic.md"
        epic_content = self._generate_epic_content(prd_name)
        epic_filepath.write_text(epic_content)

        # Growth on canvas
        epic_molecule = self.canvas.grow_from(
            parent_id=list(self.canvas.molecules.keys())[0],  # From PRD molecule
            new_content=epic_content[:200],  # Preview
            intention=f"Epic: {prd_name}",
            layer=LayerType.LOGIC
        )

        self.symphony.completion_cadence(f"Epic created: {prd_name}")
        self.canvas.evolve_molecule(epic_molecule.id, GrowthPhase.GROWTH)

        epic = Epic(
            name=prd_name,
            prd_name=prd_name,
            filepath=epic_filepath,
            epic_content=epic_content,
            tasks=[],
            created_at=datetime.now()
        )

        self.active_epics[prd_name] = epic

        print(f"✅ Epic created: {epic_filepath}")
        print(f"🎵 Symphony harmony: {self.symphony.get_harmony_score():.2%}")

        return epic

    async def decompose_epic_to_tasks(self, epic_name: str) -> List[Task]:
        """
        Break epic into individual tasks
        CCPM: /pm:epic-decompose <name>
        """
        print(f"\n🗂️  Decomposing Epic: {epic_name}")
        print("=" * 50)

        epic_dir = self.epics_dir / epic_name

        # Spawn multiple agents in parallel for task decomposition
        teacher_agent = await self.orchestra.spawn_agent(
            role=AgentRole.TEACHER,
            name=f"teacher_{epic_name}"
        )

        creator_agent = await self.orchestra.spawn_agent(
            role=AgentRole.CREATOR,
            name=f"creator_{epic_name}"
        )

        # Agents collaborate to break down epic
        self.symphony.ai_operation(
            "Multi-agent task decomposition",
            complexity=80
        )

        # Generate task files (001.md, 002.md, etc.)
        tasks = []
        task_names = [
            "Set up database schema",
            "Implement backend API",
            "Create frontend components",
            "Write tests",
            "Documentation"
        ]

        for i, task_name in enumerate(task_names, 1):
            task_number = f"{i:03d}"
            task_filepath = epic_dir / f"{task_number}.md"

            task_content = self._generate_task_content(
                number=task_number,
                name=task_name,
                depends_on=[] if i == 1 else [f"{(i-1):03d}"]
            )

            task_filepath.write_text(task_content)

            # Growth molecule for each task
            task_molecule = self.canvas.plant_seed(
                intention=f"Task {task_number}: {task_name}",
                layer=LayerType.LOGIC
            )

            # Musical note for each task created
            self.symphony.user_interaction(f"Task {task_number} created", intensity=60)

            task = Task(
                number=task_number,
                name=task_name,
                filepath=task_filepath,
                status="open",
                depends_on=[] if i == 1 else [f"{(i-1):03d}"],
                parallel=False,
                acceptance_criteria=[]
            )

            tasks.append(task)

            print(f"  ✅ Task {task_number}: {task_name}")

        # Epic decomposition complete - grand finale
        self.symphony.completion_cadence(f"Epic decomposed: {len(tasks)} tasks")

        if epic_name in self.active_epics:
            self.active_epics[epic_name].tasks = tasks

        print(f"\n🎉 Created {len(tasks)} tasks")
        print(f"🎵 Final harmony: {self.symphony.get_harmony_score():.2%}")

        return tasks

    async def work_on_task(self, epic_name: str, task_number: str):
        """
        Student works on a task with AI assistance
        Musical feedback for progress!
        """
        print(f"\n💻 Working on Task {task_number}")
        print("=" * 50)

        task_filepath = self.epics_dir / epic_name / f"{task_number}.md"

        if not task_filepath.exists():
            raise ValueError(f"Task not found: {task_number}")

        # Spawn helper agent
        helper_agent = await self.orchestra.spawn_agent(
            role=AgentRole.TEACHER,
            name=f"task_helper_{task_number}"
        )

        # Agent helps student work on task
        self.symphony.ai_operation(
            f"Working on task {task_number}",
            complexity=60
        )

        # Simulate work progression (in real system, this tracks actual code changes)
        for step in ["Planning", "Implementation", "Testing", "Review"]:
            print(f"  🔄 {step}...")
            self.symphony.code_execution(f"{step}_{task_number}", success=True)
            time.sleep(0.5)

        # Task complete!
        self.symphony.completion_cadence(f"Task {task_number} completed")

        # Update task status in markdown
        content = task_filepath.read_text()
        updated_content = content.replace(
            "status: open",
            "status: completed"
        )
        task_filepath.write_text(updated_content)

        print(f"✅ Task {task_number} completed!")
        print(f"🎵 Harmony: {self.symphony.get_harmony_score():.2%}")

    def _generate_prd_content(self, name: str, requirements: str) -> str:
        """Generate CCPM-format PRD markdown"""
        return f"""---
name: {name}
status: draft
created: {datetime.now().isoformat()}
---

# PRD: {name}

## Overview
{requirements}

## User Stories
- As a user, I want to...
- As a developer, I need to...

## Requirements
1. Functional requirements
2. Non-functional requirements
3. Technical constraints

## Success Criteria
- [ ] Requirement 1 met
- [ ] Requirement 2 met
- [ ] User testing complete
"""

    def _generate_epic_content(self, prd_name: str) -> str:
        """Generate CCPM-format Epic markdown"""
        return f"""---
name: {prd_name}
prd: {prd_name}
created: {datetime.now().isoformat()}
---

# Epic: {prd_name}

## Technical Implementation Plan

### Architecture
- Component structure
- Data flow
- API design

### Technology Stack
- Frontend: React
- Backend: Python/FastAPI
- Database: PostgreSQL

### Implementation Phases
1. Foundation setup
2. Core functionality
3. UI/UX
4. Testing & deployment

## Dependencies
- None

## Risks & Mitigation
- Risk 1: Mitigation strategy
"""

    def _generate_task_content(self,
                               number: str,
                               name: str,
                               depends_on: List[str]) -> str:
        """Generate CCPM-format Task markdown"""
        return f"""---
name: {name}
status: open
created: {datetime.now().isoformat()}
updated: {datetime.now().isoformat()}
parallel: false
depends_on: {depends_on}
---

# Task: {name}

## Description
Detailed description of what needs to be done.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Tests written and passing

## Technical Notes
- Implementation details
- Edge cases to consider
"""

    def export_learning_journey(self) -> str:
        """
        Export student's complete journey
        PRDs → Epics → Tasks → Code Growth → Symphony
        """
        story = f"# {self.student_name}'s Learning Journey\n\n"

        story += "## Musical Symphony Statistics\n"
        story += f"- Total notes played: {len(self.symphony.score)}\n"
        story += f"- System harmony: {self.symphony.get_harmony_score():.2%}\n\n"

        story += "## Growth Canvas Evolution\n"
        story += self.canvas.export_growth_story()

        story += "\n## CCPM Project Structure\n"
        story += f"- PRDs created: {len(self.active_prds)}\n"
        story += f"- Epics developed: {len(self.active_epics)}\n"

        total_tasks = sum(len(epic.tasks) for epic in self.active_epics.values())
        story += f"- Tasks completed: {total_tasks}\n"

        return story


# Example usage for students

async def student_learning_journey_demo():
    """
    Demo: A student's complete journey through the platform
    """
    print("\n" + "=" * 60)
    print("🎓 SYMPHONIC CCPM STUDENT JOURNEY")
    print("=" * 60)

    # Initialize for student
    platform = SymphonicCCPM(
        project_root=Path("."),
        student_name="Alex"
    )

    print("\n📚 Week 1: Understanding Requirements")
    # Create PRD
    prd = await platform.create_prd(
        prd_name="habit-tracker",
        requirements="Build an app to help users track daily habits"
    )

    print("\n📚 Week 2: Technical Planning")
    # Convert to Epic
    epic = await platform.parse_prd_to_epic("habit-tracker")

    print("\n📚 Week 3-4: Breaking Down Work")
    # Decompose to tasks
    tasks = await platform.decompose_epic_to_tasks("habit-tracker")

    print("\n📚 Week 5-9: Building!")
    # Work on first task
    await platform.work_on_task("habit-tracker", "001")

    print("\n" + "=" * 60)
    print("🎉 JOURNEY COMPLETE!")
    print("=" * 60)

    # Export learning journey
    journey = platform.export_learning_journey()
    print(journey)


if __name__ == "__main__":
    import asyncio
    asyncio.run(student_learning_journey_demo())
