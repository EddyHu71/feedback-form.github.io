<template>
  <div id="app">
    <h1>Feedback Form</h1>
    <form @submit.prevent="submitFeedback">
      <div v-for="(criteria, index) in feedbackCriteria" :key="index" class="rating-section">
        <label :for="criteria.name">{{ criteria.label }}</label>
        <star-rating
          v-model="criteria.rating"
          :star-size="30"
          :show-rating="true"
          :increment="1"
        ></star-rating>
      </div>
      <div>
        <label for="comments">Your comments:</label>
        <textarea id="comments" v-model="comments"></textarea>
      </div>
      <button type="submit">Submit Feedback</button>
    </form>
    <div v-if="submitted">
      <h2>Thank you for your feedback!</h2>
      <div v-for="(criteria, index) in feedbackCriteria" :key="index">
        <p><strong>{{ criteria.label }}:</strong> {{ criteria.rating }} stars</p>
      </div>
      <p><strong>Comments:</strong> {{ comments }}</p>
    </div>
  </div>
</template>
<script>

export default {
  data() {
    return {
      feedbackCriteria: [
        { name: 'Satisfication', label: 'How would you rate your satisfication with our product?', rating: 0 },
        { name: 'Enjoy', label: 'How would you enjoy to use our product?', rating: 0 },
        { name: 'Recommend', label: 'How would you recommend our product to others?', rating: 0 }
      ],
      comments: '',
      submitted: false
    };
  },
  methods: {
    submitFeedback() {
      this.submitted = true;
      console.log('Feedback:', this.feedbackCriteria);
      console.log('Comments:', this.comments);
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}

.rating-section {
  margin-bottom: 20px;
}
</style>
