# Offering Types Reference

## Overview

Select the offering type that best matches what you're proposing. This selection determines:
- Which product components to include
- Pricing structure and range
- Deliverables and timeline
- Resource allocation

---

## CONSULTING / STRATEGY

### When to Use
- Client needs strategic guidance
- Assessment and recommendations required
- Decision-making support
- No implementation included

### Typical Components
| Component | Description | Typical Allocation |
|-----------|-------------|-------------------|
| Discovery & Assessment | Understand current state | 20% of effort |
| Analysis & Strategy | Develop recommendations | 40% of effort |
| Advisory Sessions | Guide decision-making | 25% of effort |
| Documentation | Capture outcomes | 15% of effort |

### Characteristics
| Attribute | Specification |
|-----------|---------------|
| Duration | 4-12 weeks |
| Price Range | $25,000 - $75,000 |
| Primary Deliverable | Strategy document + recommendations |
| Success Metric | Decisions made, direction set |

### Deliverables
1. Current state assessment
2. Gap analysis
3. Options analysis with recommendations
4. Implementation roadmap (for client to execute)
5. Executive presentation

### Pricing Guidance
- Fixed fee preferred
- Milestone-based payments
- No success fee (consulting doesn't generate measurable savings)

---

## IMPLEMENTATION

### When to Use
- Client needs something built and deployed
- Defined scope and deliverables
- Measurable outcomes expected
- Ongoing support may be included

### Typical Components
| Component | Description | Typical Allocation |
|-----------|-------------|-------------------|
| Strategy & Design | Plan the solution | 15% of effort |
| Build & Configure | Create the solution | 45% of effort |
| Testing & QA | Ensure quality | 15% of effort |
| Deployment & Training | Go live | 15% of effort |
| Documentation | Capture for handoff | 10% of effort |

### Characteristics
| Attribute | Specification |
|-----------|---------------|
| Duration | 8-20 weeks |
| Price Range | $40,000 - $150,000+ |
| Primary Deliverable | Working solution deployed |
| Success Metric | Solution live, adoption achieved |

### Deliverables
1. Requirements documentation
2. Solution design
3. Configured/built solution
4. Testing results
5. Training materials
6. Deployment documentation
7. Support handoff

### Pricing Guidance
- Fixed fee for defined scope
- Milestone-based payments tied to deliverables
- Success fee optional (tied to measured outcomes)

---

## TRAINING / ENABLEMENT

### When to Use
- Client needs skills transfer
- Team enablement is the goal
- Methodology or framework adoption
- Limited ongoing engagement

### Typical Components
| Component | Description | Typical Allocation |
|-----------|-------------|-------------------|
| Curriculum Design | Plan the training | 20% of effort |
| Content Development | Create materials | 30% of effort |
| Delivery | Conduct training | 35% of effort |
| Assessment | Measure learning | 15% of effort |

### Characteristics
| Attribute | Specification |
|-----------|---------------|
| Duration | 2-8 weeks |
| Price Range | $10,000 - $35,000 |
| Primary Deliverable | Trained team + materials |
| Success Metric | Skills transferred, adoption achieved |

### Deliverables
1. Training curriculum
2. Training materials (slides, guides, exercises)
3. Training sessions delivered
4. Assessment results
5. Certification (if applicable)

### Pricing Guidance
- Per-person or per-session pricing
- Fixed fee for complete program
- Volume discounts for larger groups

---

## FULL ENGAGEMENT

### When to Use
- Client needs end-to-end support
- Strategy + implementation + ongoing support
- Complex, multi-phase projects
- Long-term partnership

### Typical Components
| Component | Description | Typical Allocation |
|-----------|-------------|-------------------|
| Strategy & Methodology | Set direction | 15% of effort |
| Implementation | Build solution | 35% of effort |
| Advisory & Coaching | Guide decisions | 20% of effort |
| Program Management | Coordinate work | 15% of effort |
| Training & Enablement | Transfer skills | 15% of effort |

### Characteristics
| Attribute | Specification |
|-----------|---------------|
| Duration | 12-26 weeks |
| Price Range | $75,000 - $200,000+ |
| Primary Deliverable | Transformed capability |
| Success Metric | Measurable business outcomes |

### Deliverables
1. Strategy and roadmap
2. Solution implemented
3. Team trained
4. Processes documented
5. Outcomes measured
6. Handoff complete

### Pricing Guidance
- Base investment + success fee structure
- Milestone-based payments
- Success fee tied to documented savings/outcomes

---

## Selection Decision Tree

```
START
  │
  ├── Does client need something BUILT?
  │   ├── YES → Is training/enablement a significant component?
  │   │         ├── YES → FULL ENGAGEMENT
  │   │         └── NO → IMPLEMENTATION
  │   │
  │   └── NO → Does client need ADVICE/GUIDANCE?
  │             ├── YES → Is skills transfer the primary goal?
  │             │         ├── YES → TRAINING
  │             │         └── NO → CONSULTING
  │             │
  │             └── NO → Is this primarily SKILLS TRANSFER?
  │                       ├── YES → TRAINING
  │                       └── NO → Re-evaluate requirements
```

---

## Combining Offering Types

You can combine offering types for complex engagements:

| Combination | Use Case | Pricing Approach |
|-------------|----------|------------------|
| CONSULTING + IMPLEMENTATION | Strategy leading to build | Phase-based, strategy fixed, implementation scoped |
| IMPLEMENTATION + TRAINING | Build with enablement | Package together, training bundled |
| CONSULTING + TRAINING | Strategy with capability building | Separate phases, can be sequential |
| FULL ENGAGEMENT | All components | Base + success fee structure |

---

## Pricing Model Structure

### Base Investment Components

Configure your pricing model with these standard components:

```json
{
  "components": [
    {
      "id": "STRATEGY",
      "name": "Strategy & Methodology",
      "description": "Framework, governance, decision support",
      "base_price": "[YOUR PRICE]"
    },
    {
      "id": "IMPLEMENTATION",
      "name": "Implementation",
      "description": "Build, configure, deploy",
      "base_price": "[YOUR PRICE]"
    },
    {
      "id": "CONSULTING",
      "name": "Strategic Consulting",
      "description": "Advisory, coaching, decisions",
      "base_price": "[YOUR PRICE]"
    },
    {
      "id": "TRAINING",
      "name": "Training & Enablement",
      "description": "Skills transfer, materials, certification",
      "base_price": "[YOUR PRICE]"
    },
    {
      "id": "PM",
      "name": "Program Management",
      "description": "Coordination, tracking, accountability",
      "base_price": "[YOUR PRICE]"
    }
  ]
}
```

### Success Fee Structure (Optional)

For implementation and full engagement offerings:

```json
{
  "success_fee": {
    "percentage": 25,
    "basis": "Year 1 documented savings",
    "cap": "[YOUR CAP]",
    "minimum": 0,
    "trigger": "Documented savings exceed base investment"
  }
}
```

---

## ROI Calculation Framework

For each offering type, calculate ROI using:

### Inputs
- **Current State Cost**: Client's current spend on this function/process
- **Hours Involved**: Weekly/monthly hours consumed
- **Hourly Rate**: Blended cost of those hours
- **Error/Rework Cost**: Additional costs from current inefficiencies

### Calculation
```
Annual Current Cost = (Hours/week × 52 × Hourly Rate) + Error Costs
Expected Savings = Annual Current Cost × Improvement %
Break-even = Base Investment ÷ (Monthly Savings)
Year 1 ROI = (Expected Savings - Base Investment) ÷ Base Investment × 100
```

### Typical Improvement Percentages by Offering
| Offering | Typical Improvement |
|----------|---------------------|
| CONSULTING | 10-25% (indirect) |
| IMPLEMENTATION | 30-50% (direct) |
| TRAINING | 15-30% (capability) |
| FULL ENGAGEMENT | 40-60% (comprehensive) |

---

*End of Offering Types Reference*
